
import Sidebar from '../components/Sidebar';
import Topbar from '../components/Topbar';
import '../styles/sidebar.css';
import '../styles/topbar.css';
import '../styles/layout.css';

function MainLayout({ children }) {
  return (
    <div className="app-layout">
      <Sidebar />

      <div className="main-area">
        <Topbar />

        <main className="main-content">
          {children}
        </main>
      </div>
    </div>
  );
}

export default MainLayout;
