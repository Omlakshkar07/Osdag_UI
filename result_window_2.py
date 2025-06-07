import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QSplitter, QFrame, QSizePolicy, QAction, QToolBar, QStackedWidget,
    QDockWidget, QScrollArea, QMenu, QLineEdit, QGroupBox
)
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QIcon, QFont, QColor, QPalette, QPixmap


class CloseableTabWidget(QTabWidget):
    """Custom tab widget with closeable tabs"""
    
    def __init__(self, parent=None):
        super(CloseableTabWidget, self).__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)
        self.setDocumentMode(True)
        self.setMovable(True)
        
    def closeTab(self, index):
        """Close the tab at the given index"""
        # Don't actually remove tabs in this demo
        print(f"Close tab requested for tab index {index}")


class TreePanel(QWidget):
    """Project details tree panel implementation"""
    
    def __init__(self, parent=None):
        super(TreePanel, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create header
        header = QFrame()
        header.setFrameShape(QFrame.StyledPanel)
        # Updated header background color to match the image (light brown/beige)
        header.setStyleSheet("background-color: #F0E6D2;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(5, 5, 5, 5)
        
        title_label = QLabel("Project Details Window")
        title_label.setStyleSheet("color: #333333; font-weight: bold;")
        header_layout.addWidget(title_label)
        
        close_btn = QPushButton("×")
        close_btn.setFixedSize(20, 20)
        close_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                color: #555555;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                color: #000000;
            }
        """)
        header_layout.addWidget(close_btn)
        
        layout.addWidget(header)
        
        # Create tree widget
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setStyleSheet("""
            QTreeWidget {
                border: none;
                background-color: #F9F5ED;  /* Updated to a lighter beige to match image */
            }
            QTreeWidget::item {
                height: 24px;
            }
            QTreeWidget::item:selected {
                background-color: #D6E5D6;  /* Lighter green for selected items */
                color: #000000;
            }
            QTreeWidget::item:has-children {
                font-weight: bold;
                color: #333333;
            }
        """)
        
        # Input Parameters section
        input_params = QTreeWidgetItem(["Input Parameters"])
        input_params.setIcon(0, QIcon.fromTheme("folder", self.getDefaultIcon()))
        input_params.setBackground(0, QColor("#F9F5ED"))  # Set background for Input Parameters
        input_params.setForeground(0, QColor("#333333"))  # Dark text color
        self.tree.addTopLevelItem(input_params)
        
        # Structure Works Data
        structure_works = QTreeWidgetItem(["Structure Works Data"])
        structure_works.setIcon(0, QIcon.fromTheme("folder", self.getDefaultIcon()))
        structure_works.setForeground(0, QColor("#333333"))  # Dark text color
        input_params.addChild(structure_works)
        
        structure_works.addChild(self.createItem("Financial Data"))
        structure_works.addChild(self.createItem("Carbon Emission Data"))
        structure_works.addChild(self.createItem("Bridge and Traffic Data"))
        structure_works.addChild(self.createItem("Maintenance and Repair"))
        structure_works.addChild(self.createItem("Demolition and Recycling"))
        
        # Output section
        output = QTreeWidgetItem(["Output"])
        output.setIcon(0, QIcon.fromTheme("folder", self.getDefaultIcon()))
        output.setBackground(0, QColor("#F9F5ED"))  # Set background for Output
        output.setForeground(0, QColor("#333333"))  # Dark text color
        self.tree.addTopLevelItem(output)
        
        # Output items with updated icons to match those in the image (document icons)
        output_items = [
            "Initial Construction Cost",
            "Initial Carbon Emission Cost",
            "Time Cost",
            "Traffic User Cost",
            "Carbon Emission due to Re-routing",
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
            item = self.createItem(item_text, is_document=True)
            output.addChild(item)
        
        # Expand input params by default
        input_params.setExpanded(True)
        structure_works.setExpanded(True)
        output.setExpanded(True)
        
        layout.addWidget(self.tree)
        
    def createItem(self, text, is_document=False):
        """Create a tree item with the appropriate icon"""
        item = QTreeWidgetItem([text])
        if is_document:
            # Document icon for output items
            item.setIcon(0, QIcon.fromTheme("text-x-generic", self.getDocumentIcon()))
        else:
            # Default folder icon
            item.setIcon(0, QIcon.fromTheme("folder", self.getDefaultIcon()))
        return item
    
    def getDefaultIcon(self):
        """Return a default folder icon"""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(0, 0, 0, 0))
        return QIcon(pixmap)
    
    def getDocumentIcon(self):
        """Return a default document icon"""
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(0, 0, 0, 0))
        return QIcon(pixmap)


class DataWindowPanel(QWidget):
    """Data Window Panel Implementation"""
    
    def __init__(self, parent=None):
        super(DataWindowPanel, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Added proper margins to match image
        
        # Life-Cycle Costs label
        title_label = QLabel("Life-Cycle Costs for 50 years")
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Placeholder for chart area - upper section (donut charts area)
        chart_placeholder = QWidget()
        chart_placeholder.setMinimumHeight(250)  # Adjusted height to match image
        chart_placeholder.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CCCCCC;")
        
        chart_layout = QHBoxLayout(chart_placeholder)  # Changed to HBoxLayout for horizontal arrangement
        
        # Create 3 placeholders for donuts as shown in the image
        for i, (title, color) in enumerate([
            ("Economic cost distribution across\nvarious stages for PSC bridges for 50 years", "#E0D6C0"),
            ("Social cost distribution across\nstages for PSC bridges for 50 years", "#D6D6E9"),
            ("Environmental cost distribution across\nstages for PSC bridges for 50 years", "#D6E9D6")
        ]):
            donut = QFrame()
            donut.setStyleSheet(f"background-color: {color}; border: 1px solid #DDDDDD;")
            donut_layout = QVBoxLayout(donut)
            
            # Close button in top right
            close_container = QWidget()
            close_layout = QHBoxLayout(close_container)
            close_layout.setContentsMargins(0, 0, 0, 0)
            close_layout.addStretch()
            
            close_btn = QPushButton("×")
            close_btn.setFixedSize(16, 16)
            close_btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-color: transparent;
                    color: #555555;
                    font-weight: bold;
                    font-size: 12px;
                }
            """)
            close_layout.addWidget(close_btn)
            donut_layout.addWidget(close_container)
            
            # Title
            title_lbl = QLabel(title)
            title_lbl.setAlignment(Qt.AlignCenter)
            title_lbl.setStyleSheet("font-size: 10px;")
            donut_layout.addWidget(title_lbl)
            
            # Placeholder for donut
            donut_placeholder = QLabel("⭕")  # Simple placeholder
            donut_placeholder.setAlignment(Qt.AlignCenter)
            donut_placeholder.setStyleSheet("font-size: 72px;")
            donut_layout.addWidget(donut_placeholder)
            
            chart_layout.addWidget(donut)
        
        layout.addWidget(chart_placeholder)
        
        # Create legend - matching the image style
        legend_frame = QFrame()
        legend_frame.setMaximumHeight(30)
        legend_frame.setStyleSheet("background-color: #F8F8F8;")
        
        legend_layout = QHBoxLayout(legend_frame)
        legend_layout.setSpacing(15)  # Add space between legend items
        
        legend_items = [
            ("Initial Stage", "#000080"),  # Dark blue
            ("Use Stage", "#006400"),      # Dark green
            ("End-of-Life Stage", "#8B4513"), # Brown
            ("Beyond-Life Stage", "#90EE90")  # Light green
        ]
        
        for text, color in legend_items:
            color_box = QFrame()
            color_box.setFixedSize(12, 12)
            color_box.setStyleSheet(f"background-color: {color}; border: 1px solid black;")
            
            label = QLabel(text)
            label.setStyleSheet("font-size: 11px;")
            
            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(5)
            item_layout.addWidget(color_box)
            item_layout.addWidget(label)
            
            legend_layout.addLayout(item_layout)
        
        legend_layout.addStretch()
        layout.addWidget(legend_frame)
        
        # Horizontal bar chart - matching image style
        barchart_placeholder = QWidget()
        barchart_placeholder.setMinimumHeight(300)
        barchart_placeholder.setStyleSheet("background-color: #FFFFFF;")
        
        barchart_layout = QVBoxLayout(barchart_placeholder)
        
        # Create placeholder for horizontal bars
        for i, (label, value, color) in enumerate([
            ("Initial Construction Cost", "91.83", "#4CAF50"),
            ("Initial Carbon Emission Cost", "8.53", "#8BC34A"),
            ("Time Cost", "2.32", "#CDDC39"),
            ("Traffic User Cost", "109.13", "#FFC107"),
            ("Carbon Emission due to Re-Routing", "29.03", "#FF9800"),
            ("Periodic Maintenance Costs", "1.44", "#FF5722"),
            ("Maintenance Emission Costs", "0.23", "#F44336"),
            ("Routine Inspection Costs", "15.32", "#E91E63"),
            ("Repair & Rehabilitation Cost", "1.08", "#9C27B0"),
            ("Demolition & Disposal Cost", "0.77", "#673AB7"),
            ("Recycling Cost", "0", "#3F51B5")
        ]):
            bar_row = QWidget()
            bar_layout = QHBoxLayout(bar_row)
            bar_layout.setContentsMargins(0, 2, 0, 2)
            
            # Label
            bar_label = QLabel(label)
            bar_label.setFixedWidth(200)
            bar_label.setStyleSheet("font-size: 11px;")
            bar_layout.addWidget(bar_label)
            
            # Bar
            bar_frame = QFrame()
            bar_value = float(value)
            bar_width = min(int(bar_value * 3), 300)  # Scale for visibility
            bar_frame.setFixedSize(bar_width, 15)
            bar_frame.setStyleSheet(f"background-color: {color};")
            bar_layout.addWidget(bar_frame)
            
            # Value
            value_label = QLabel(value)
            value_label.setStyleSheet("font-size: 11px;")
            bar_layout.addWidget(value_label)
            
            bar_layout.addStretch()
            barchart_layout.addWidget(bar_row)
        
        # Total row
        total_row = QWidget()
        total_layout = QHBoxLayout(total_row)
        total_layout.setContentsMargins(0, 5, 0, 5)
            
        # Label
        total_label = QLabel("Total Life-Cycle Cost")
        total_label.setFixedWidth(200)
        total_label.setStyleSheet("font-size: 11px; font-weight: bold;")
        total_layout.addWidget(total_label)
            
        # Bar
        total_frame = QFrame()
        total_frame.setFixedSize(300, 15)
        total_frame.setStyleSheet("background-color: #424242;")
        total_layout.addWidget(total_frame)
            
        # Value
        total_value_label = QLabel("259.15")
        total_value_label.setStyleSheet("font-size: 11px; font-weight: bold;")
        total_layout.addWidget(total_value_label)
            
        total_layout.addStretch()
        barchart_layout.addWidget(total_row)
        
        layout.addWidget(barchart_placeholder)
        
        # Total cost display
        total_frame = QFrame()
        total_layout = QHBoxLayout(total_frame)
        total_layout.setContentsMargins(5, 5, 5, 5)
        
        total_layout.addStretch()
        
        total_label = QLabel("Total Life-Cycle Cost:")
        total_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        total_layout.addWidget(total_label)
        
        total_value = QLabel("259.15 Lakh")
        total_value.setStyleSheet("font-weight: bold; font-size: 12px;")
        total_layout.addWidget(total_value)
        
        layout.addWidget(total_frame)
        
        # Download and view options
        options_frame = QFrame()
        options_layout = QVBoxLayout(options_frame)
        
        # Download options
        download_layout = QHBoxLayout()
        download_layout.addStretch()
        
        for format in ["Download as PNG", "Download as JPG", "Download as PDF"]:
            btn = QPushButton(format)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #C0C0C0;
                    border-radius: 2px;
                    padding: 3px 8px;
                    font-size: 11px;
                }
            """)
            download_layout.addWidget(btn)
        
        options_layout.addLayout(download_layout)
        
        # View options
        view_layout = QHBoxLayout()
        view_layout.addStretch()
        
        for view_type in ["View as Pie Chart", "View as Table"]:
            btn = QPushButton(view_type)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #C0C0C0;
                    border-radius: 2px;
                    padding: 3px 8px;
                    font-size: 11px;
                }
            """)
            view_layout.addWidget(btn)
        
        options_layout.addLayout(view_layout)
        
        layout.addWidget(options_frame)
        
        # Navigation buttons - matching the image
        nav_frame = QFrame()
        nav_layout = QHBoxLayout(nav_frame)
        
        nav_layout.addStretch()
        
        back_btn = QPushButton("Back")
        back_btn.setFixedWidth(80)
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
                border-radius: 2px;
                padding: 5px;
            }
        """)
        nav_layout.addWidget(back_btn)
        
        next_btn = QPushButton("Next")
        next_btn.setFixedWidth(80)
        next_btn.setStyleSheet("""
            QPushButton {
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
                border-radius: 2px;
                padding: 5px;
            }
        """)
        nav_layout.addWidget(next_btn)
        
        layout.addWidget(nav_frame)


class ResultsWindowPanel(QWidget):
    """Results Window Panel Implementation"""
    
    def __init__(self, parent=None):
        super(ResultsWindowPanel, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # Added proper margins to match image
        
        # Create tabbed widget for Economic, Social, Environmental costs
        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setStyleSheet("""
            QTabBar::tab {
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
                padding: 4px 12px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: none;
            }
        """)
        
        # Economic cost tab
        economic_tab = QWidget()
        economic_layout = QVBoxLayout(economic_tab)
        
        cost_title = QLabel("Economic cost distribution across various stages for bridges for 50 years")
        cost_title.setAlignment(Qt.AlignCenter)
        cost_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        economic_layout.addWidget(cost_title)
        
        chart_placeholder = QWidget()
        chart_placeholder.setMinimumHeight(250)
        chart_placeholder.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CCCCCC;")
        
        chart_text = QLabel("⭕")  # Simple donut placeholder
        chart_text.setAlignment(Qt.AlignCenter)
        chart_text.setStyleSheet("font-size: 72px;")
        chart_layout = QVBoxLayout(chart_placeholder)
        chart_layout.addWidget(chart_text)
        
        economic_layout.addWidget(chart_placeholder)
        
        # Download options
        dl_layout = QHBoxLayout()
        dl_layout.addStretch()
        
        for format in ["Download as PNG", "Download as JPG", "Download as PDF"]:
            btn = QPushButton(format)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #C0C0C0;
                    border-radius: 2px;
                    padding: 3px 8px;
                    font-size: 11px;
                }
            """)
            dl_layout.addWidget(btn)
        
        economic_layout.addLayout(dl_layout)
        
        # View options
        view_layout = QHBoxLayout()
        view_layout.addStretch()
        
        for view_type in ["View as Pie Chart", "View as Table"]:
            btn = QPushButton(view_type)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #F0F0F0;
                    border: 1px solid #C0C0C0;
                    border-radius: 2px;
                    padding: 3px 8px;
                    font-size: 11px;
                }
            """)
            view_layout.addWidget(btn)
        
        economic_layout.addLayout(view_layout)
        
        tabs.addTab(economic_tab, "Economic Cost")
        
        # Social cost tab
        social_tab = QWidget()
        social_layout = QVBoxLayout(social_tab)
        
        social_title = QLabel("Social cost distribution across stages for PSC bridges for 50 years")
        social_title.setAlignment(Qt.AlignCenter)
        social_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        social_layout.addWidget(social_title)
        
        social_chart = QWidget()
        social_chart.setMinimumHeight(250)
        social_chart.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CCCCCC;")
        social_layout.addWidget(social_chart)
        
        tabs.addTab(social_tab, "Social Cost")
        
        # Environmental cost tab
        env_tab = QWidget()
        env_layout = QVBoxLayout(env_tab)
        
        env_title = QLabel("Environmental cost distribution across stages for PSC bridges for 50 years")
        env_title.setAlignment(Qt.AlignCenter)
        env_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        env_layout.addWidget(env_title)
        
        env_chart = QWidget()
        env_chart.setMinimumHeight(250)
        env_chart.setStyleSheet("background-color: #FFFFFF; border: 1px solid #CCCCCC;")
        env_layout.addWidget(env_chart)
        
        tabs.addTab(env_tab, "Environmental Cost")
        
        layout.addWidget(tabs)


class BLCCAStudio(QMainWindow):
    """Main BLCCA Studio application window"""
    
    def __init__(self):
        super(BLCCAStudio, self).__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle("BLCCA Studio 1.0.0")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create menu bar - matching green header in image
        self.createMenuBar()
        
        # Create toolbar
        self.createToolBar()
        
        # Create tab bar for main navigation
        self.createTopTabBar()
        
        # Create main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Removed margins to match image
        main_layout.setSpacing(0)
        
        # Create splitter for resizable panels
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(1)  # Thin splitter handle to match image
        splitter.setStyleSheet("QSplitter::handle { background-color: #CCCCCC; }")
        
        # Left panel - Project Details
        project_panel = TreePanel()
        project_panel.setMinimumWidth(170)  # Adjusted to match image
        project_panel.setMaximumWidth(250)  # Limited maximum width
        project_panel.setStyleSheet("background-color: #F9F5ED;")  # Lighter beige to match image
        splitter.addWidget(project_panel)
        
        # Right side panel container
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        
        # Create tab widget for Data Window and Results Window
        right_tabs = CloseableTabWidget()
        right_tabs.setStyleSheet("""
            QTabWidget::pane {
                border-top: 1px solid #C0C0C0;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #E0E0E0;
                border: 1px solid #C0C0C0;
                border-bottom: none;
                padding: 4px 8px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: white;
            }
            QTabBar::close-button {
                image: url(close.png);
                subcontrol-position: right;
            }
        """)
        
        # Data Window tab
        data_tab = QScrollArea()
        data_tab.setWidgetResizable(True)
        data_tab.setWidget(DataWindowPanel())
        data_tab.setStyleSheet("background-color: white; border: none;")
        right_tabs.addTab(data_tab, "Data Window")
        
        # Results Window tab
        results_tab = QScrollArea()
        results_tab.setWidgetResizable(True)
        results_tab.setWidget(ResultsWindowPanel())
        results_tab.setStyleSheet("background-color: white; border: none;")
        right_tabs.addTab(results_tab, "Results Window")
        
        right_layout.addWidget(right_tabs)
        splitter.addWidget(right_panel)
        
        # Set initial splitter sizes - left panel gets 1/6, right gets 5/6 to match image
        splitter.setSizes([200, 1000])
        
        main_layout.addWidget(splitter)
        
        # Updated application style to match image
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F0F0F0;
            }
            QMenuBar {
                background-color: #4CAF50;  /* Green color to match header in image */
                color: white;
                padding: 2px;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 12px;
            }
            QMenuBar::item:selected {
                background-color: rgba(255, 255, 255, 0.2);
            }
            QToolBar {
                background-color: #F0F0F0;
                border: none;
                spacing: 3px;
            }
            QToolButton {
                background-color: transparent;
                border: none;
                padding: 3px;
            }
            QToolButton:hover {
                background-color: #E0E0E0;
                border-radius: 2px;
            }
            QPushButton {
                background-color: #F0F0F0;
                border: 1px solid #C0C0C0;
                border-radius: 2px;
                padding: 4px;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
        """)
    
    def createMenuBar(self):
        """Create the application menu bar - green colored to match image"""
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: #4CAF50;
                color: white;
            }
            QMenuBar::item {
                background-color: transparent;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: rgba(255, 255, 255, 0.2);
            }
        """)
        
        # File menu
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(self.createAction('New', 'Create a new project'))
        fileMenu.addAction(self.createAction('Open', 'Open an existing project'))
        fileMenu.addAction(self.createAction('Save', 'Save the current project'))
        fileMenu.addSeparator()
        fileMenu.addAction(self.createAction('Exit', 'Exit the application'))
        
        # Home menu
        homeMenu = menubar.addMenu('Home')
        
        # Reports menu
        reportsMenu = menubar.addMenu('Reports')
        
        # Help menu
        helpMenu = menubar.addMenu('Help')
    
    def createToolBar(self):
        """Create the application toolbar - matching the image style"""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(24, 24))  # Larger icons to match image
        toolbar.setMovable(False)
        toolbar.setStyleSheet("background-color: #F5F5F5; border: none;")
        
        # Tool buttons with simple square placeholders (matching image)
        for icon_name in ["⚙️", "📁", "📄"]:
            action = QAction(icon_name, self)
            action.setStatusTip(f"{icon_name} action")
            toolbar.addAction(action)
        
        self.addToolBar(toolbar)
    
    def createTopTabBar(self):
        """Create the top tab bar for main navigation - matching image style"""
        tabBar = QTabWidget()
        tabBar.setDocumentMode(True)
        tabBar.setTabPosition(QTabWidget.North)
        
        # Create more centered navigation tabs with proper styling to match image
        tabBar.setStyleSheet("""
            QTabWidget::pane {
                border: none;
            }
            QTabBar {
                alignment: center;
            }
            QTabBar::tab {
                padding: 4px 16px;
                margin: 0;
                background-color: #F0F0F0;
                border: 1px solid #D0D0D0;
                border-bottom: 1px solid white;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: none;
            }
        """)
        
        # Create the tabs to match image
        tabBar.addTab(QWidget(), "Windows")
        tabBar.addTab(QWidget(), "Tutorials")
        tabBar.addTab(QWidget(), "Project Details")
        tabBar.addTab(QWidget(), "Results")
        tabBar.addTab(QWidget(), "Compare")
        
        # Add tab bar below the toolbar with centered alignment
        tabBarContainer = QWidget()
        tabBarContainer.setStyleSheet("background-color: #F5F5F5;")
        layout = QHBoxLayout(tabBarContainer)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)  # Center the tab widget in the container
        layout.addWidget(tabBar)
        
        # Create a dock widget to hold the tab bar
        dock = QDockWidget("", self)
        dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        dock.setWidget(tabBarContainer)
        dock.setTitleBarWidget(QWidget())  # Hide the title bar
        
        self.addDockWidget(Qt.TopDockWidgetArea, dock)
    
    def createAction(self, text, statusTip):
        """Create a QAction with the given text and status tip"""
        action = QAction(text, self)
        action.setStatusTip(statusTip)
        return action


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BLCCAStudio()
    window.show()
    sys.exit(app.exec_())