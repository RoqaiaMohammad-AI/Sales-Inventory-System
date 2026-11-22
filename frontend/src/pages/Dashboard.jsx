import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

import '../styles/dashboard.css';

import {
  DollarSign,
  ShoppingCart,
  Package,
  Users,
  ArrowUpLeft,
  ArrowDownLeft,
  AlertTriangle,
  Clock,
  ArrowLeft,
} from 'lucide-react';

const statistics = [
  {
    title: 'إجمالي المبيعات',
    value: '12,850',
    unit: 'ر.س',
    change: '+12.5%',
    trend: 'up',
    icon: DollarSign,
    color: 'green',
    description: 'مقارنة بالشهر السابق',
  },
  {
    title: 'عدد الطلبات',
    value: '248',
    unit: 'طلب',
    change: '+8.2%',
    trend: 'up',
    icon: ShoppingCart,
    color: 'orange',
    description: 'مقارنة بالشهر السابق',
  },
  {
    title: 'المنتجات',
    value: '1,284',
    unit: 'منتج',
    change: '-2.4%',
    trend: 'down',
    icon: Package,
    color: 'purple',
    description: 'مقارنة بالشهر السابق',
  },
  {
    title: 'العملاء',
    value: '856',
    unit: 'عميل',
    change: '+5.7%',
    trend: 'up',
    icon: Users,
    color: 'blue',
    description: 'مقارنة بالشهر السابق',
  },
];

const salesChartData = [
  { day: 'السبت', sales: 1200 },
  { day: 'الأحد', sales: 2100 },
  { day: 'الاثنين', sales: 1800 },
  { day: 'الثلاثاء', sales: 2800 },
  { day: 'الأربعاء', sales: 2200 },
  { day: 'الخميس', sales: 3500 },
  { day: 'الجمعة', sales: 2900 },
];

const recentSales = [
  {
    invoice: '#INV-1025',
    customer: 'أحمد محمد',
    date: '21 نوفمبر 2026',
    amount: '1,250 ر.س',
    status: 'مكتملة',
  },
  {
    invoice: '#INV-1024',
    customer: 'سارة عبدالله',
    date: '21 نوفمبر 2026',
    amount: '850 ر.س',
    status: 'مكتملة',
  },
  {
    invoice: '#INV-1023',
    customer: 'محمد خالد',
    date: '20 نوفمبر 2026',
    amount: '2,400 ر.س',
    status: 'قيد المعالجة',
  },
  {
    invoice: '#INV-1022',
    customer: 'نورة علي',
    date: '20 نوفمبر 2026',
    amount: '620 ر.س',
    status: 'مكتملة',
  },
];

function Dashboard() {
  return (
    <div className="dashboard">
      <div className="dashboard-welcome">
        <div>
          <h2>نظرة عامة على المتجر</h2>
          <p>تابع أداء متجرك ومؤشرات المبيعات والمخزون.</p>
        </div>

        <button className="dashboard-date-button">
          <Clock size={16} />
          آخر 30 يوماً
        </button>
      </div>

      <section className="stats-grid">
        {statistics.map((item) => {
          const Icon = item.icon;

          return (
            <article className="stat-card" key={item.title}>
              <div className="stat-card-top">
                <div className={`stat-icon ${item.color}`}>
                  <Icon size={21} />
                </div>

                <span className={`stat-change ${item.trend}`}>
                  {item.trend === 'up' ? (
                    <ArrowUpLeft size={14} />
                  ) : (
                    <ArrowDownLeft size={14} />
                  )}
                  {item.change}
                </span>
              </div>

              <p className="stat-title">{item.title}</p>

              <div className="stat-value">
                <strong>{item.value}</strong>
                <span>{item.unit}</span>
              </div>

              <p className="stat-description">{item.description}</p>
            </article>
          );
        })}
      </section>

      <section className="dashboard-panels">
        <article className="panel sales-chart-panel">
          <div className="panel-header">
            <div>
              <h3>تحليل المبيعات</h3>
              <p>أداء المبيعات خلال الفترة المحددة</p>
            </div>

            <button className="panel-filter">
              أسبوعي
            </button>
          </div>

          <div className="sales-chart">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={salesChartData}
                margin={{ top: 10, right: 5, left: 5, bottom: 5 }}
              >
                <CartesianGrid
                  strokeDasharray="3 3"
                  vertical={false}
                  stroke="#eeeeef"
                />

                <XAxis
                  dataKey="day"
                  axisLine={false}
                  tickLine={false}
                  tick={{ fill: '#6b7280', fontSize: 11 }}
                />

                <YAxis
                  orientation="right"
                  axisLine={false}
                  tickLine={false}
                  tick={{ fill: '#9ca3af', fontSize: 10 }}
                />

                <Tooltip
                  formatter={(value) => [
                    `${Number(value).toLocaleString('en-US')} ر.س`,
                    'المبيعات',
                  ]}
                  contentStyle={{
                    borderRadius: '8px',
                    border: '1px solid #eeeeef',
                    fontSize: '12px',
                  }}
                />

                <Bar
                  dataKey="sales"
                  fill="#F97316"
                  radius={[5, 5, 0, 0]}
                  maxBarSize={42}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </article>

        <article className="panel inventory-panel">
          <div className="panel-header">
            <div>
              <h3>تنبيهات المخزون</h3>
              <p>المنتجات التي تحتاج إلى متابعة</p>
            </div>
          </div>

          <div className="inventory-alert">
            <div className="alert-icon danger">
              <AlertTriangle size={19} />
            </div>
            <div className="alert-details">
              <strong>منتجات منخفضة المخزون</strong>
              <span>8 منتجات تحتاج إلى إعادة طلب</span>
            </div>
            <span className="alert-count">8</span>
          </div>

          <div className="inventory-alert">
            <div className="alert-icon warning">
              <Package size={19} />
            </div>
            <div className="alert-details">
              <strong>منتجات نفدت من المخزون</strong>
              <span>3 منتجات غير متوفرة حالياً</span>
            </div>
            <span className="alert-count">3</span>
          </div>

          <a href="/inventory" className="panel-link">
            عرض المخزون
            <ArrowLeft size={15} />
          </a>
        </article>
      </section>

      <section className="panel recent-sales-panel">
        <div className="panel-header">
          <div>
            <h3>أحدث المبيعات</h3>
            <p>آخر الفواتير المسجلة في النظام</p>
          </div>

          <a href="/sales" className="panel-link">
            عرض جميع المبيعات
            <ArrowLeft size={15} />
          </a>
        </div>

        <div className="table-wrapper">
          <table className="dashboard-table">
            <thead>
              <tr>
                <th>رقم الفاتورة</th>
                <th>العميل</th>
                <th>التاريخ</th>
                <th>المبلغ</th>
                <th>الحالة</th>
              </tr>
            </thead>

            <tbody>
              {recentSales.map((sale) => (
                <tr key={sale.invoice}>
                  <td className="invoice-number">{sale.invoice}</td>
                  <td>{sale.customer}</td>
                  <td>{sale.date}</td>
                  <td className="sale-amount">{sale.amount}</td>
                  <td>
                    <span
                      className={`status-badge ${
                        sale.status === 'مكتملة' ? 'success' : 'pending'
                      }`}
                    >
                      {sale.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

export default Dashboard;
