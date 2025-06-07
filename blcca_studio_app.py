import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QTreeWidget, QTreeWidgetItem, QTabWidget, QDockWidget,
                            QToolBar, QAction, QPushButton, QFrame, QSplitter, QScrollArea,
                            QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPainter, QColor, QBrush, QPen
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class PieChartWidget(QWidget):
    def __init__(self, title, data, labels, colors, parent=None):
        super().__init__(parent)
        self.title = title
        self.data = data
        self.labels = labels
        self.colors = colors
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Title label
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(title_label)
        
        # Create matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        
        # Create the pie chart
        wedges, texts, autotexts = self.ax.pie(
            self.data, 
            colors=self.colors,
            autopct='%1.1f%%',
            startangle=90,
            wedgeprops={'edgecolor': 'w', 'linewidth': 1},
            textprops={'fontsize': 8}
        )
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        self.ax.axis('equal')
        
        # Remove the default matplotlib frame
        self.figure.patch.set_facecolor('none')
        self.ax.set_facecolor('none')
        
        # Add legend
        self.ax.legend(wedges, self.labels, loc="center right", fontsize=8)
        
        # Add the canvas to the layout
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)


class BarChartWidget(QWidget):
    def __init__(self, title, data, labels, colors, parent=None):
        super().__init__(parent)
        self.title = title
        self.data = data
        self.labels = labels
        self.colors = colors
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Title label
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-weight: bold;")
        layout.addWidget(title_label)
        
        # Create matplotlib Figure and Canvas
        self.figure, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvas(self.figure)
        
        # Create the bar chart
        y_pos = np.arange(len(self.labels))
        bars = self.ax.barh(y_pos, self.data, color=self.colors)
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(self.labels, fontsize=8)
        self.ax.invert_yaxis()  # labels read top-to-bottom
        
        # Add values to the end of each bar
        for i, bar in enumerate(bars):
            width = bar.get_width()
            self.ax.text(width + 1, bar.get_y() + bar.get_height()/2, 
                    f'{self.data[i]}', va='center', fontsize=8)
        
        # Remove the default matplotlib frame
        self.figure.patch.set_facecolor('none')
        self.ax.set_facecolor('none')
        
        # Remove spines
        for spine in self.ax.spines.values():
            spine.set_visible(False)
            
        # Add grid lines
        self.ax.xaxis.grid(True, linestyle='--', alpha=0.7)
        
        # Add the canvas to the layout
        layout.addWidget(self.canvas)
        
        # Total cost label
        total = sum(self.data)
        total_label = QLabel(f"Total Life-Cycle Cost: {total} Lakh")
        total_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        total_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(total_label)
        
        self.setLayout(layout)


class BLCCAStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle('BLCCA Studio 1.0')
        self.setGeometry(100, 100, 1200, 800)
        
        # Set main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QVBoxLayout(self.central_widget)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create tab widget for different views
        tab_widget = QTabWidget()
        tab_widget.addTab(QWidget(), "Windows")
        tab_widget.addTab(QWidget(), "Tutorials")
        tab_widget.addTab(QWidget(), "Project Details")
        tab_widget.addTab(QWidget(), "Results")
        tab_widget.addTab(QWidget(), "Compare")
        tab_widget.setCurrentIndex(0)  # Set default tab
        main_layout.addWidget(tab_widget)
        
        # Create main splitter for dockable windows
        main_splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(main_splitter)
        
        # Create Project Details Dock Window
        project_details = QWidget()
        project_layout = QVBoxLayout(project_details)
        
        # Project Details Header
        project_header = QLabel("Project Details Window")
        project_header.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        project_layout.addWidget(project_header)
        
        # Create tree widget for parameters
        tree = QTreeWidget()
        tree.setHeaderLabel("Input Parameters")
        
        # Add items to the tree
        structure_item = QTreeWidgetItem(["Structure Works Data"])
        financial_item = QTreeWidgetItem(["Financial Data"])
        emission_item = QTreeWidgetItem(["Carbon Emission Data"])
        traffic_item = QTreeWidgetItem(["Bridge and Traffic Data"])
        maintenance_item = QTreeWidgetItem(["Maintenance and Repair"])
        demolition_item = QTreeWidgetItem(["Demolition and Recycling"])
        
        tree.addTopLevelItem(structure_item)
        tree.addTopLevelItem(financial_item)
        tree.addTopLevelItem(emission_item)
        tree.addTopLevelItem(traffic_item)
        tree.addTopLevelItem(maintenance_item)
        tree.addTopLevelItem(demolition_item)
        
        project_layout.addWidget(tree)
        
        # Output section
        output_label = QLabel("Output")
        output_label.setAlignment(Qt.AlignCenter)
        output_label.setStyleSheet("background-color: #e0e0e0; padding: 5px;")
        project_layout.addWidget(output_label)
        
        # Create tree widget for output items
        output_tree = QTreeWidget()
        output_tree.setHeaderHidden(True)
        
        # Add items to the output tree
        output_items = [
            "Initial Construction Cost",
            "Initial Carbon Emission Cost",
            "Time Cost",
            "User Time Cost",
            "Carbon Emission due to Re-Routing",
            "Periodic Maintenance Costs",
            "Maintenance Emission Costs",
            "Routine Inspection Costs",
            "Repair & Rehabilitation Costs",
            "Reconstruction Costs",
            "Demolition & Disposal Cost",
            "Recycling Cost",
            "Total Life-Cycle Cost"
        ]
        
        for item_text in output_items:
            item = QTreeWidgetItem([item_text])
            output_tree.addTopLevelItem(item)
        
        project_layout.addWidget(output_tree)
        
        # Add project details to the main splitter
        main_splitter.addWidget(project_details)
        
        # Create Data Window
        data_window = QWidget()
        data_layout = QVBoxLayout(data_window)
        
        # Data Window Header
        data_header = QLabel("Data Window")
        data_header.setStyleSheet("background-color: #f0f0f0; padding: 5px;")
        data_layout.addWidget(data_header)
        
        # Create charts section
        charts_widget = QWidget()
        charts_layout = QHBoxLayout(charts_widget)
        
        # Economic cost pie chart
        economic_data = [28.4, 64.15, 7.45]
        economic_labels = ["Initial Stage", "Use Stage", "End-of-Life Stage"]
        economic_colors = ['#3366cc', '#109618', '#ff9900']
        economic_pie = PieChartWidget(
            "Economic cost distribution across\nvarious stages for bridges for 50 years",
            economic_data, economic_labels, economic_colors
        )
        charts_layout.addWidget(economic_pie)
        
        # Social cost pie chart
        social_data = [54.82, 40.18, 5.0]
        social_labels = ["Initial Stage", "Use Stage", "End-of-Life Stage"]
        social_colors = ['#dc3912', '#990099', '#0099c6']
        social_pie = PieChartWidget(
            "Social cost distribution across\nstages for PSC bridges for 50 years",
            social_data, social_labels, social_colors
        )
        charts_layout.addWidget(social_pie)
        
        # Environmental cost pie chart
        env_data = [16.65, 76.03, 7.32]
        env_labels = ["Initial Stage", "Use Stage", "End-of-Life Stage"]
        env_colors = ['#dd4477', '#66aa00', '#b82e2e']
        env_pie = PieChartWidget(
            "Environmental cost distribution across\nstages for PSC bridges for 50 years",
            env_data, env_labels, env_colors
        )
        charts_layout.addWidget(env_pie)
        
        data_layout.addWidget(charts_widget)
        
        # Legend for stages
        legend_widget = QWidget()
        legend_layout = QHBoxLayout(legend_widget)
        
        stages = ["Initial Stage", "Use Stage", "End-of-Life Stage", "Beyond-Life Stage"]
        colors = ["#000080", "#006400", "#8B4513", "#4B0082"]
        
        for stage, color in zip(stages, colors):
            stage_layout = QHBoxLayout()
            
            color_box = QFrame()
            color_box.setFixedSize(15, 15)
            color_box.setStyleSheet(f"background-color: {color}; border: 1px solid black;")
            
            stage_label = QLabel(stage)
            
            stage_layout.addWidget(color_box)
            stage_layout.addWidget(stage_label)
            stage_layout.addStretch()
            
            temp_widget = QWidget()
            temp_widget.setLayout(stage_layout)
            legend_layout.addWidget(temp_widget)
        
        legend_layout.addStretch()
        data_layout.addWidget(legend_widget)
        
        # Bar chart for life-cycle costs
        cost_labels = [
            "Initial Construction Cost",
            "Initial Carbon Emission Cost",
            "Time Cost", 
            "User Time Cost",
            "Carbon Emission due to Re-Routing",
            "Periodic Maintenance Costs",
            "Maintenance Emission Cost",
            "Routine Inspection Cost",
            "Repair & Rehabilitation Cost",
            "Demolition & Disposal Cost",
            "Recycling Cost"
        ]
        cost_data = [49.83, 8.53, 123.19, 29.03, 1.44, 16.99, 14.52, 1.95, 5.77, 8.0]
        cost_colors = ['#3366cc', '#dc3912', '#ff9900', '#109618', '#990099', '#0099c6', 
                      '#dd4477', '#66aa00', '#b82e2e', '#316395', '#994499']
        
        bar_chart = BarChartWidget(
            "Life-Cycle Costs for 50 years",
            cost_data[:len(cost_labels)-1],  # One less data point than labels
            cost_labels[:-1],  # Remove the last label
            cost_colors[:-1]   # Remove the last color
        )
        data_layout.addWidget(bar_chart)
        
        # Navigation buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        back_button = QPushButton("Back")
        next_button = QPushButton("Next")
        
        button_layout.addWidget(back_button)
        button_layout.addWidget(next_button)
        
        data_layout.addLayout(button_layout)
        
        # Add data window to the main splitter
        main_splitter.addWidget(data_window)
        
        # Set the stretch factors
        main_splitter.setStretchFactor(0, 1)  # Project Details
        main_splitter.setStretchFactor(1, 3)  # Data Window
        
        # Show the window
        self.show()
    
    def create_menu_bar(self):
        """Create the menu bar with File, Home, Reports and Help menus"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('File')
        
        # Home menu
        home_menu = menubar.addMenu('Home')
        
        # Reports menu
        reports_menu = menubar.addMenu('Reports')
        
        # Help menu
        help_menu = menubar.addMenu('Help')
    
    def create_toolbar(self):
        """Create the toolbar with basic actions"""
        toolbar = QToolBar()
        toolbar.setMovable(False)
        
        # Add toolbar actions without icons to avoid potential issues
        folder_action = QAction("Open Folder", self)
        document_action = QAction("New Document", self)
        save_action = QAction("Save", self)
        
        toolbar.addAction(folder_action)
        toolbar.addAction(document_action)
        toolbar.addAction(save_action)
        
        self.addToolBar(toolbar)


if __name__ == '__main__':
    try:
        print("Starting BLCCA Studio application...")
        app = QApplication(sys.argv)
        print("QApplication created")
        ex = BLCCAStudio()
        print("BLCCAStudio instance created")
        print("Showing main window...")
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
