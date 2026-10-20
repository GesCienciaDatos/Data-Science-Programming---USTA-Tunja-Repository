import { ref } from 'vue';
import { translations, courseTranslations } from './translations.js';

// Global reactive language state initialized from localStorage
const storedLang = typeof window !== 'undefined' ? localStorage.getItem('usta_lang') : null;
export const currentLang = ref(storedLang === 'en' ? 'en' : 'es');

// Synchronize document element language attribute
if (typeof document !== 'undefined') {
  document.documentElement.lang = currentLang.value;
}

export function useI18n() {
  function setLanguage(lang) {
    if (lang === 'es' || lang === 'en') {
      currentLang.value = lang;
      if (typeof window !== 'undefined') {
        localStorage.setItem('usta_lang', lang);
      }
      if (typeof document !== 'undefined') {
        document.documentElement.lang = lang;
      }
    }
  }

  function toggleLanguage() {
    setLanguage(currentLang.value === 'es' ? 'en' : 'es');
    return currentLang.value;
  }

  function t(path, params = {}) {
    const lang = currentLang.value;
    const keys = path.split('.');
    
    let val = translations[lang];
    for (const k of keys) {
      if (val && typeof val === 'object' && k in val) {
        val = val[k];
      } else {
        // Fallback to Spanish if key not found
        let fallback = translations['es'];
        for (const fk of keys) {
          if (fallback && typeof fallback === 'object' && fk in fallback) {
            fallback = fallback[fk];
          } else {
            return path;
          }
        }
        val = fallback;
        break;
      }
    }

    if (typeof val === 'string') {
      let str = val;
      for (const [pk, pv] of Object.entries(params)) {
        str = str.replace(new RegExp(`{${pk}}`, 'g'), String(pv));
      }
      return str;
    }
    return val !== undefined ? val : path;
  }

  /**
   * Returns localized course metadata for the web interface.
   * NOTE: Notebooks themselves are NEVER modified, preserving the authentic repository code.
   */
  function getCourseLocalized(course) {
    if (!course) return course;
    if (currentLang.value === 'es') return course;

    const trans = courseTranslations[course.id];
    if (!trans) return course;

    return {
      ...course,
      name: trans.name || course.name,
      title: trans.title || course.title,
      description: trans.description || course.description,
      badge: trans.badge || course.badge,
      semester: trans.semester || course.semester
    };
  }

  return {
    currentLang,
    setLanguage,
    toggleLanguage,
    t,
    getCourseLocalized
  };
}
