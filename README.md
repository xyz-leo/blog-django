# Django CMS Blog — A Modular and Extensible Content Management Platform

This project is a fully structured mini-CMS built with Django, designed to mimic the architecture and workflows of real production content systems.  
Although it includes a complete blog engine, the codebase goes far beyond a simple CRUD application: it emphasizes **modularity**, **extensibility**, **security**, **clean separation of concerns**, and realistic **production-grade patterns**.

The project serves as both a strong portfolio piece and a scalable foundation for future expansion.

---

## Core Features

### 1. Dynamic Content Model Architecture

The platform provides multiple content types with clean routing and admin integrations:

- **Posts**
- **Pages**
- **Categories**
- **Tags**

Each model uses automatic slug generation, metadata fields, publication flags, and reusable mixins to ensure consistency and extensibility across the entire CMS.

---

## Blog Engine

### 2. Full Blog Workflow

The blog subsystem includes:

- Paginated post listing  
- Detailed post view (cover image, excerpt, body content, metadata)  
- Tag, category, and author filtering  
- Adaptive homepage based on context  
- SEO-friendly slug routing

### 3. Search System

A dedicated full-text search engine for posts, built with Django `Q` objects:

- Searches across title, excerpt, and body  
- Integrated pagination  
- Clean `/search/` route  
- Graceful fallback for empty queries

### 4. Syntax Highlighting (CodeMirror Integration)

CodeMirror enables syntax-highlighted code blocks inside posts:

- Supports `data-language="python"` and other languages  
- Fully integrated into the admin content editor  
- Sanitization rules preserve only essential attributes

---

## Admin & Content Editing

### 5. Rich Text Editing with Summernote

The Django admin uses Summernote to allow structured editing with formatting, links, images, and embedded media.

### 6. Content Sanitization with Bleach

A sanitization layer ensures content safety:

- Unsafe HTML and scripts removed  
- Only whitelisted tags/attributes allowed  
- CodeMirror attributes preserved  
- Sanitization occurs before saving

---

## Layout and Frontend Architecture

### 7. Component-Based Templates

The frontend uses a fully modular structure:

- Partials for header, footer, menus, hero sections, pagination, and UI components  
- Dedicated CSS for each page  
- Clear separation of layout, structure, and logic

### 8. Theme Switching (Light/Dark)

A custom JS-powered theme system:

- User preference stored with `localStorage`  
- Theme applied globally on load  
- Modular, theme-specific CSS

---

## Security & Environment Management

### 9. Environment Variables with python-dotenv

Environment variables are centralized in `.env` files:

- Loaded in both `settings.py` and `wsgi.py`  
- Consistent behavior across shells and deployment environments  
- Keeps secrets out of the repository

### 10. Brute-Force Protection with Django-Axes

Django-Axes provides authentication hardening:

- Limits repeated failed login attempts  
- Automatic account lockouts  
- Cool-off periods to slow brute force attacks  
- Middleware + authentication backend integration  

This closely mirrors real production security workflows.

---

## Pagination and Navigation

### 11. Global Pagination

All listing views use a unified pagination system with shared templates and styling:

- Home  
- Categories  
- Tags  
- Authors  
- Search results  

---

## Project Structure and Maintainability

### 12. Clean Modular Architecture

The codebase follows production-inspired conventions:

- Reusable template partials  
- Clear app separation  
- Dedicated static assets per component  
- Shared utilities for publishing logic  
- Well-organized URL routing and namespacing  
- Maintainable folder layout

---

## Docker Support

A fully functional Docker setup provides:

- Reproducible, isolated development  
- Consistent environment for deployment  
- Faster onboarding for contributors

---

## Project Structure
```
├── data
│ ├── postgres
│ │ └── data
│ └── web
│ ├── media
│ └── static
├── djangoapp
│ ├── blog
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── init.py
│ │ ├── migrations
│ │ ├── models.py
│ │ ├── static
│ │ ├── templates
│ │ ├── tests.py
│ │ ├── urls.py
│ │ └── views.py
│ ├── manage.py
│ ├── project
│ │ ├── asgi.py
│ │ ├── init.py
│ │ ├── pycache
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── requirements.txt
│ ├── site_setup
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── context_processors.py
│ │ ├── init.py
│ │ ├── migrations
│ │ ├── models.py
│ │ ├── tests.py
│ │ └── views.py
│ └── utils
│ ├── model_validators.py
│ ├── resize_images.py
│ ├── sanitize.py
│ └── slug_creator.py
├── docker-compose.yml
├── Dockerfile
├── dotenv
├── README.md
├── scripts
│ ├── collectstatic.sh
│ ├── commands.sh
│ ├── makemigrations.sh
│ ├── migrate.sh
│ ├── runserver.sh
│ └── wait_psql.sh
```

---

## How to Run the Project (Docker)

Follow the steps below after cloning the repository.

### 1. Install Docker and Docker Compose

Ensure Docker and Docker Compose are installed on your system.

Enable and start the Docker service:

```sh
sudo systemctl enable --now docker
```

### 2. Add Your User to the Docker Group

This allows you to run Docker without using `sudo`:

```sh
sudo usermod -aG docker $USER
```

Log out and log back in for the change to take effect.

### 3. Fix Permissions for Data Folders (If Needed)

Some environments require adjusting folder ownership:

```sh
sudo chown -R $USER:$USER data/web
```

### 4. Build and Start the Containers

```sh
docker-compose up --build
```

### 5. Apply Database Migrations

```sh
docker-compose run --rm djangoapp python manage.py migrate
```

### 6. Create a Superuser

```sh
docker-compose run --rm djangoapp python manage.py createsuperuser
```

### 7. Access the Admin Panel

http://localhost:8000/admin/

### 8. Initial Site Setup

1. Open the Site Setup section.
2. Create the initial configuration object.
3. The blog frontend will start rendering correctly once this is set.

### 9. Optional: Collect Static Files for Production

```sh
docker-compose run --rm djangoapp python manage.py collectstatic
```

---

## Disclaimer

This project was created for learning, experimentation, and portfolio demonstration, but intentionally follows real-world patterns used in production-grade Django systems.
