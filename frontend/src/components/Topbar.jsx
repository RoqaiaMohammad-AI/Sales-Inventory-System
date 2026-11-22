
import {
  Search,
  Bell,
  Globe,
  ChevronDown,
  Menu,
} from 'lucide-react';

function Topbar() {
  return (
    <header className="topbar">
      <div className="topbar-right">
        <button className="mobile-menu-button" aria-label="فتح القائمة">
          <Menu size={21} />
        </button>

        <div className="page-heading">
          <h1>لوحة التحكم</h1>
          <p>مرحباً بك، إليك ملخص أداء متجرك اليوم</p>
        </div>
      </div>

      <div className="topbar-left">
        <div className="topbar-search">
          <Search size={18} />
          <input
            type="search"
            placeholder="ابحث عن منتج، فاتورة، عميل..."
            aria-label="بحث"
          />
          <kbd>Ctrl K</kbd>
        </div>

        <button className="topbar-icon-button" aria-label="الإشعارات">
          <Bell size={20} />
          <span className="notification-dot"></span>
        </button>

        <button className="language-button">
          <Globe size={18} />
          <span>العربية</span>
          <ChevronDown size={15} />
        </button>

        <div className="topbar-divider"></div>

        <button className="user-profile">
          <div className="user-avatar">م</div>
          <div className="user-details">
            <strong>مدير النظام</strong>
            <span>Administrator</span>
          </div>
          <ChevronDown size={15} />
        </button>
      </div>
    </header>
  );
}

export default Topbar;
