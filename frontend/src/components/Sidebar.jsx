
import {
  LayoutDashboard,
  Package,
  Tags,
  Warehouse,
  ShoppingCart,
  ShoppingBag,
  Users,
  Truck,
  RotateCcw,
  BarChart3,
  UserCog,
  Settings,
  Store,
  ChevronLeft,
} from 'lucide-react';

const menuItems = [
  {
    title: 'الرئيسية',
    icon: LayoutDashboard,
    path: '/',
  },
  {
    title: 'إدارة المنتجات',
    icon: Package,
    path: '/products',
  },
  {
    title: 'التصنيفات',
    icon: Tags,
    path: '/categories',
  },
  {
    title: 'المخزون',
    icon: Warehouse,
    path: '/inventory',
  },
  {
    title: 'المبيعات',
    icon: ShoppingCart,
    path: '/sales',
  },
  {
    title: 'المشتريات',
    icon: ShoppingBag,
    path: '/purchases',
  },
  {
    title: 'العملاء',
    icon: Users,
    path: '/customers',
  },
  {
    title: 'الموردون',
    icon: Truck,
    path: '/suppliers',
  },
  {
    title: 'المرتجعات',
    icon: RotateCcw,
    path: '/returns',
  },
  {
    title: 'التقارير والتحليلات',
    icon: BarChart3,
    path: '/reports',
  },
  {
    title: 'المستخدمون والصلاحيات',
    icon: UserCog,
    path: '/users',
  },
];

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">
          <Store size={23} />
        </div>

        <div className="brand-info">
          <h2>StockFlow</h2>
          <span>إدارة المبيعات والمخزون</span>
        </div>
      </div>

      <div className="sidebar-section-title">
        القائمة الرئيسية
      </div>

      <nav className="sidebar-nav">
        {menuItems.map((item, index) => {
          const Icon = item.icon;
          const isActive = index === 0;

          return (
            <a
              key={item.path}
              href={item.path}
              className={`sidebar-link ${isActive ? 'active' : ''}`}
            >
              <Icon size={19} strokeWidth={1.8} />
              <span>{item.title}</span>

              {isActive && (
                <ChevronLeft size={16} className="active-arrow" />
              )}
            </a>
          );
        })}
      </nav>

      <div className="sidebar-bottom">
        <a href="/settings" className="sidebar-link">
          <Settings size={19} strokeWidth={1.8} />
          <span>الإعدادات</span>
        </a>

        <div className="sidebar-version">
          <span>StockFlow</span>
          <span>الإصدار 1.0.0</span>
        </div>
      </div>
    </aside>
  );
}

export default Sidebar;
