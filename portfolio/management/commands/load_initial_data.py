from django.core.management.base import BaseCommand
from portfolio.models import (
    Skill, Project, Certification, Publication, SiteConfiguration
)
from datetime import date


class Command(BaseCommand):
    help = 'Load initial portfolio data for Varun K N'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading initial data...')
        
        # Site Configuration
        config = SiteConfiguration.get_config()
        config.about_description = """AI-focused Integrated MCA student with strong foundation in Python, Machine Learning, and Deep Learning. 

Experienced in model experimentation, dataset preprocessing, feature engineering, hyperparameter tuning, cross-validation, and performance evaluation using real-world datasets. 

Published IEEE research in deep learning-based object detection. Passionate about building reproducible, data-driven AI solutions and contributing to research-oriented development."""
        config.save()
        self.stdout.write(self.style.SUCCESS('✓ Site configuration loaded'))
        
        # Skills
        skills_data = [
            # Programming
            ('Python', 'programming', 95),
            ('SQL', 'programming', 80),
            ('Java', 'programming', 75),
            ('C', 'programming', 70),
            
            # Data Processing
            ('Pandas', 'data', 90),
            ('NumPy', 'data', 90),
            ('Data Cleaning', 'data', 85),
            ('Feature Engineering', 'data', 85),
            ('EDA', 'data', 80),
            
            # Machine Learning
            ('XGBoost', 'ml', 90),
            ('CatBoost', 'ml', 85),
            ('Random Forest', 'ml', 85),
            ('Linear Regression', 'ml', 80),
            ('K-Means Clustering', 'ml', 80),
            ('PCA', 'ml', 75),
            
            # Deep Learning
            ('YOLOv8', 'dl', 90),
            ('YOLOv6-v9', 'dl', 85),
            ('CNN', 'dl', 80),
            ('OpenCV', 'dl', 85),
            
            # Tools
            ('Jupyter Notebook', 'tools', 95),
            ('Google Colab', 'tools', 90),
            ('Git', 'tools', 85),
            ('Docker', 'tools', 75),
            ('VS Code', 'tools', 90),
        ]
        
        for name, category, proficiency in skills_data:
            Skill.objects.get_or_create(
                name=name,
                category=category,
                defaults={'proficiency': proficiency}
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(skills_data)} skills loaded'))

        # Projects
        projects_data = [
            {
                'title': 'Rental Vacancy Intelligence Platform',
                'short_description': 'Predictive analytics system for rental vacancy classification and rent estimation using Django & AI',
                'description': '''Developed a comprehensive predictive analytics system for rental vacancy classification and rent estimation.

• Implemented XGBoost classifier with 91.5% validation accuracy for vacancy prediction
• Built CatBoost regression model achieving R² score of 0.93 for rent estimation
• Performed extensive data preprocessing, feature engineering, and hyperparameter tuning
• Conducted K-Fold cross-validation and comprehensive model comparison
• Designed REST APIs to deploy and serve real-time model predictions using Django''',
                'technologies': 'Python, XGBoost, CatBoost, Django, REST API, Pandas, NumPy',
                'date_completed': date(2025, 3, 1),
                'featured': True,
                'accuracy': '91.5% accuracy',
                'metric_1_label': 'R² Score',
                'metric_1_value': '0.93',
                'status': 'completed'
            },
            {
                'title': 'Environmental Conservation Using Deep Learning',
                'short_description': 'YOLOv8-based forest fire and smoke detection system with optimization',
                'description': '''Built an intelligent forest fire and smoke detection system using aerial imagery and deep learning.

• Developed YOLOv8-based detection model achieving mAP@0.5 = 0.789
• Applied dataset augmentation and threshold experimentation for improved accuracy
• Designed transportation optimization model using PuLP for resource allocation
• Minimized firefighting response time and operational costs
• Generated risk-zone maps and optimal drone path visualizations for decision support''',
                'technologies': 'YOLOv8, Python, OpenCV, PuLP, Optimization, Computer Vision',
                'date_completed': date(2024, 12, 1),
                'featured': True,
                'accuracy': 'mAP@0.5 = 0.789',
                'metric_1_label': 'Detection Speed',
                'metric_1_value': 'Real-time',
                'status': 'completed'
            },
            {
                'title': 'Bike Rental Demand Prediction',
                'short_description': 'ML-based demand forecasting using Seoul bike-sharing dataset',
                'description': '''Analyzed Seoul bike-sharing dataset with weather and temporal features for demand prediction.

• Engineered cyclic time features and encoded categorical variables
• Compared Linear Regression (R²=0.58), Random Forest (R²=0.94), and XGBoost (R²=0.93)
• Evaluated performance using RMSE, MAE, and cross-validation techniques
• Performed feature importance analysis to interpret model behavior
• Documented comprehensive findings and model comparison''',
                'technologies': 'Python, Random Forest, XGBoost, Scikit-learn, Pandas, Matplotlib',
                'date_completed': date(2025, 4, 1),
                'featured': True,
                'accuracy': 'R² = 0.94',
                'metric_1_label': 'RMSE',
                'metric_1_value': 'Low',
                'status': 'completed'
            },
            {
                'title': 'Customer Segmentation Using K-Means',
                'short_description': 'Unsupervised learning for customer clustering with PCA analysis',
                'description': '''Implemented customer segmentation using K-Means clustering and dimensionality reduction.

• Preprocessed 200-record dataset using scaling and standardization
• Determined optimal clusters (K=5) using Elbow Method
• Achieved Silhouette Score of 0.444 without PCA and 0.388 with PCA
• Applied PCA for dimensionality reduction and cluster visualization
• Proposed improvements using DBSCAN and t-SNE techniques''',
                'technologies': 'Python, K-Means, PCA, Scikit-learn, Pandas, Seaborn',
                'date_completed': date(2025, 2, 1),
                'featured': False,
                'metric_1_label': 'Silhouette Score',
                'metric_1_value': '0.444',
                'status': 'completed'
            }
        ]
        
        for project_data in projects_data:
            Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(projects_data)} projects loaded'))

        # Certifications
        certifications_data = [
            {
                'title': 'Tata Group Data Analytics Job Simulation',
                'issuer': 'Tata Group',
                'issue_date': date(2025, 12, 1),
            },
            {
                'title': 'AWS Academy Cloud Architecting',
                'issuer': 'AWS Academy (Credly Verified)',
                'issue_date': date(2025, 5, 1),
            },
            {
                'title': 'Microsoft Azure AI Essentials',
                'issuer': 'Microsoft (LinkedIn Learning)',
                'issue_date': date(2025, 4, 1),
            },
            {
                'title': 'Google Cloud Computing Foundations',
                'issuer': 'Google Cloud (Credly Verified)',
                'issue_date': date(2025, 6, 1),
            }
        ]
        
        for cert_data in certifications_data:
            Certification.objects.get_or_create(
                title=cert_data['title'],
                defaults=cert_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(certifications_data)} certifications loaded'))
        
        # Publications
        publications_data = [
            {
                'title': 'Real-Time Snake Detection and Recognition Systems in Videos Using Deep Learning',
                'authors': 'Varun K N, et al.',
                'conference': 'IEEE ICNEWS 2024',
                'year': 2024,
                'abstract': '''Proposed and implemented a comprehensive deep learning framework using YOLOv6–YOLOv9 models for real-time snake detection and segmentation in video streams. Achieved mAP greater than 0.85 for detection tasks and mAP greater than 0.94 for segmentation tasks. Conducted comparative experimentation across multiple model variants to analyze performance trade-offs. The research provides insights into practical deployment of object detection systems for wildlife monitoring and safety applications.''',
                'keywords': 'Deep Learning, YOLO, Object Detection, Computer Vision, Real-time Systems'
            }
        ]
        
        for pub_data in publications_data:
            Publication.objects.get_or_create(
                title=pub_data['title'],
                defaults=pub_data
            )
        self.stdout.write(self.style.SUCCESS(f'✓ {len(publications_data)} publications loaded'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 All initial data loaded successfully!'))
