-- Tabla principal de posts
CREATE TABLE wp_posts (
  ID BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  post_author BIGINT(20) UNSIGNED NOT NULL DEFAULT 1,
  post_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  post_date_gmt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  post_content LONGTEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  post_title TEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  post_excerpt TEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  post_status VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'publish',
  comment_status VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'closed',
  ping_status VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'closed',
  post_password VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  post_name VARCHAR(200) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  to_ping TEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  pinged TEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  post_modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  post_modified_gmt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  post_content_filtered LONGTEXT COLLATE utf8mb4_unicode_ci NOT NULL,
  post_parent BIGINT(20) UNSIGNED NOT NULL DEFAULT 0,
  guid VARCHAR(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  menu_order INT(11) NOT NULL DEFAULT 0,
  post_type VARCHAR(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'attachment',
  post_mime_type VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'application/pdf',
  comment_count BIGINT(20) NOT NULL DEFAULT 0,
  PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabla de metadatos
CREATE TABLE wp_postmeta (
  meta_id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  post_id BIGINT(20) UNSIGNED NOT NULL,
  meta_key VARCHAR(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  meta_value LONGTEXT COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (meta_id),
  KEY post_id (post_id),
  KEY meta_key (meta_key(191))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- tabla term_relationships
CREATE TABLE wp_term_relationships (
  object_id BIGINT(20) UNSIGNED NOT NULL DEFAULT 0,
  term_taxonomy_id BIGINT(20) UNSIGNED NOT NULL DEFAULT 0,
  term_order INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (object_id, term_taxonomy_id),
  KEY term_taxonomy_id (term_taxonomy_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
