import os  
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "logistics_system"

list_of_files = [
    # GitHub workflows
    ".github/workflows/.gitkeep",
    
    # Backend structure
    "backend/__init__.py",
    "backend/app/__init__.py",
    "backend/app/main.py",
    "backend/app/config.py",
    
    # API structure with role-based endpoints
    "backend/app/api/__init__.py",
    "backend/app/api/deps.py",
    "backend/app/api/v1/__init__.py",
    "backend/app/api/v1/api.py",
    
    # Dispatcher endpoints
    "backend/app/api/v1/endpoints/dispatcher/__init__.py",
    "backend/app/api/v1/endpoints/dispatcher/orders.py",
    "backend/app/api/v1/endpoints/dispatcher/dispatch.py",
    "backend/app/api/v1/endpoints/dispatcher/warehouse.py",
    "backend/app/api/v1/endpoints/dispatcher/inventory.py",
    "backend/app/api/v1/endpoints/dispatcher/drivers.py",
    
    # Driver endpoints
    "backend/app/api/v1/endpoints/driver/__init__.py",
    "backend/app/api/v1/endpoints/driver/deliveries.py",
    "backend/app/api/v1/endpoints/driver/tracking.py",
    "backend/app/api/v1/endpoints/driver/route.py",
    "backend/app/api/v1/endpoints/driver/status.py",
    
    # Customer endpoints
    "backend/app/api/v1/endpoints/customer/__init__.py",
    "backend/app/api/v1/endpoints/customer/orders.py",
    "backend/app/api/v1/endpoints/customer/tracking.py",
    "backend/app/api/v1/endpoints/customer/profile.py",
    
    # Auth endpoints (shared)
    "backend/app/api/v1/endpoints/auth/__init__.py",
    "backend/app/api/v1/endpoints/auth/login.py",
    "backend/app/api/v1/endpoints/auth/register.py",
    
    # Core
    "backend/app/core/__init__.py",
    "backend/app/core/config.py",
    "backend/app/core/security.py",
    
    # Database
    "backend/app/db/__init__.py",
    "backend/app/db/base.py",
    "backend/app/db/session.py",
    
    # Models (SQLAlchemy)
    "backend/app/models/__init__.py",
    "backend/app/models/shipment.py",
    "backend/app/models/order.py",
    "backend/app/models/inventory.py",
    "backend/app/models/warehouse.py",
    "backend/app/models/tracking.py",
    "backend/app/models/user.py",
    "backend/app/models/driver.py",
    "backend/app/models/customer.py",
    "backend/app/models/dispatcher.py",
    "backend/app/models/delivery.py",
    "backend/app/models/route.py",
    
    # Schemas (Pydantic)
    "backend/app/schemas/__init__.py",
    "backend/app/schemas/shipment.py",
    "backend/app/schemas/order.py",
    "backend/app/schemas/inventory.py",
    "backend/app/schemas/warehouse.py",
    "backend/app/schemas/tracking.py",
    "backend/app/schemas/user.py",
    "backend/app/schemas/driver.py",
    "backend/app/schemas/customer.py",
    "backend/app/schemas/dispatcher.py",
    "backend/app/schemas/delivery.py",
    "backend/app/schemas/route.py",
    
    # CRUD operations
    "backend/app/crud/__init__.py",
    "backend/app/crud/base.py",
    "backend/app/crud/shipment.py",
    "backend/app/crud/order.py",
    "backend/app/crud/inventory.py",
    "backend/app/crud/warehouse.py",
    "backend/app/crud/driver.py",
    "backend/app/crud/customer.py",
    "backend/app/crud/delivery.py",
    
    # Services (Business Logic)
    "backend/app/services/__init__.py",
    "backend/app/services/shipment_service.py",
    "backend/app/services/order_service.py",
    "backend/app/services/embedding_service.py",
    "backend/app/services/tracking_service.py",
    "backend/app/services/dispatch_service.py",
    "backend/app/services/route_service.py",
    "backend/app/services/notification_service.py",
    
    # Embeddings
    "backend/app/embeddings/__init__.py",
    "backend/app/embeddings/vector_db.py",
    "backend/app/embeddings/embedder.py",
    "backend/app/embeddings/search.py",
    
    # Utils
    "backend/app/utils/__init__.py",
    "backend/app/utils/helpers.py",
    "backend/app/utils/validators.py",
    "backend/app/utils/logger.py",
    
    # Backend requirements
    "backend/requirements.txt",
    
    # ==================== DISPATCHER FRONTEND ====================
    "frontend/dispatcher/pages/index.html",
    "frontend/dispatcher/pages/dashboard.html",
    "frontend/dispatcher/pages/orders.html",
    "frontend/dispatcher/pages/dispatch.html",
    "frontend/dispatcher/pages/warehouse.html",
    "frontend/dispatcher/pages/inventory.html",
    "frontend/dispatcher/pages/drivers.html",
    "frontend/dispatcher/pages/analytics.html",
    
    "frontend/dispatcher/css/style.css",
    "frontend/dispatcher/css/dashboard.css",
    "frontend/dispatcher/css/components.css",
    
    "frontend/dispatcher/js/app.js",
    "frontend/dispatcher/js/api.js",
    "frontend/dispatcher/js/config.js",
    "frontend/dispatcher/js/utils.js",
    "frontend/dispatcher/js/modules/dashboard.js",
    "frontend/dispatcher/js/modules/orders.js",
    "frontend/dispatcher/js/modules/dispatch.js",
    "frontend/dispatcher/js/modules/warehouse.js",
    "frontend/dispatcher/js/modules/drivers.js",
    
    "frontend/dispatcher/components/navbar.html",
    "frontend/dispatcher/components/sidebar.html",
    "frontend/dispatcher/components/footer.html",
    
    "frontend/dispatcher/assets/images/.gitkeep",
    "frontend/dispatcher/assets/icons/.gitkeep",
    
    # ==================== DRIVER FRONTEND ====================
    "frontend/driver/pages/index.html",
    "frontend/driver/pages/dashboard.html",
    "frontend/driver/pages/deliveries.html",
    "frontend/driver/pages/current-delivery.html",
    "frontend/driver/pages/route.html",
    "frontend/driver/pages/history.html",
    "frontend/driver/pages/profile.html",
    
    "frontend/driver/css/style.css",
    "frontend/driver/css/dashboard.css",
    "frontend/driver/css/components.css",
    "frontend/driver/css/mobile.css",
    
    "frontend/driver/js/app.js",
    "frontend/driver/js/api.js",
    "frontend/driver/js/config.js",
    "frontend/driver/js/utils.js",
    "frontend/driver/js/modules/dashboard.js",
    "frontend/driver/js/modules/deliveries.js",
    "frontend/driver/js/modules/tracking.js",
    "frontend/driver/js/modules/route.js",
    "frontend/driver/js/modules/navigation.js",
    
    "frontend/driver/components/navbar.html",
    "frontend/driver/components/header.html",
    "frontend/driver/components/footer.html",
    
    "frontend/driver/assets/images/.gitkeep",
    "frontend/driver/assets/icons/.gitkeep",
    
    # ==================== CUSTOMER FRONTEND ====================
    "frontend/customer/pages/index.html",
    "frontend/customer/pages/dashboard.html",
    "frontend/customer/pages/create-order.html",
    "frontend/customer/pages/my-orders.html",
    "frontend/customer/pages/track-order.html",
    "frontend/customer/pages/order-history.html",
    "frontend/customer/pages/profile.html",
    "frontend/customer/pages/support.html",
    
    "frontend/customer/css/style.css",
    "frontend/customer/css/dashboard.css",
    "frontend/customer/css/components.css",
    "frontend/customer/css/responsive.css",
    
    "frontend/customer/js/app.js",
    "frontend/customer/js/api.js",
    "frontend/customer/js/config.js",
    "frontend/customer/js/utils.js",
    "frontend/customer/js/modules/dashboard.js",
    "frontend/customer/js/modules/orders.js",
    "frontend/customer/js/modules/tracking.js",
    "frontend/customer/js/modules/profile.js",
    
    "frontend/customer/components/navbar.html",
    "frontend/customer/components/sidebar.html",
    "frontend/customer/components/footer.html",
    
    "frontend/customer/assets/images/.gitkeep",
    "frontend/customer/assets/icons/.gitkeep",
    
    # ==================== SHARED FRONTEND ====================
    "frontend/shared/css/common.css",
    "frontend/shared/css/auth.css",
    "frontend/shared/js/auth.js",
    "frontend/shared/js/constants.js",
    "frontend/shared/components/login.html",
    "frontend/shared/components/register.html",
    
    # Static files (served by FastAPI)
    "static/uploads/.gitkeep",
    
    # Data directories
    "data/vector_store/.gitkeep",
    "data/uploads/.gitkeep",
    
    # Logs
    "logs/.gitkeep",
    
    # Tests
    "tests/__init__.py",
    "tests/test_api/__init__.py",
    "tests/test_api/test_dispatcher.py",
    "tests/test_api/test_driver.py",
    "tests/test_api/test_customer.py",
    "tests/test_api/test_auth.py",
    "tests/test_embeddings/__init__.py",
    "tests/test_embeddings/test_vector_search.py",
    
    # Research/trials
    "research/trials.ipynb",
    "research/embedding_experiments.ipynb",
    "research/route_optimization.ipynb",
    
    # Config files
    "config/config.yaml",
    "config/database.yaml",
    "config/roles.yaml",
    "params.yaml",
    "dvc.yaml",
    
    # Root files
    ".env.example",
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "docker-compose.yml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info(f"\n{project_name} folder structure created successfully!")
logging.info("\n📁 Structure Overview:")
logging.info("├── Backend: FastAPI with role-based endpoints")
logging.info("├── Frontend:")
logging.info("│   ├── Dispatcher Interface (Order management, dispatch)")
logging.info("│   ├── Driver Interface (Deliveries, tracking, routes)")
logging.info("│   └── Customer Interface (Place orders, track shipments)")
logging.info("└── Shared: Common components & auth\n")
logging.info("🚀 Next steps:")
logging.info("1. Create virtual environment: python -m venv venv")
logging.info("2. Activate venv and install dependencies")
logging.info("3. Configure .env file")