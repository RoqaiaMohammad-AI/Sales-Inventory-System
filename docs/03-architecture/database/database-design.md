# تصميم قاعدة البيانات
# Database Design

## 1. معلومات عامة

- اسم المشروع: نظام إدارة المبيعات والمخزون (Sales & Inventory Management System).
- اسم قاعدة البيانات: `sales_inventory_db`.
- نظام إدارة قواعد البيانات: MySQL.
- نوع قاعدة البيانات: Relational Database.
- عدد الجداول: 18 جدولاً.
- نوع المفاتيح الأساسية: `BIGINT UNSIGNED` مع `AUTO_INCREMENT`.
- ترميز البيانات: يعتمد على إعدادات قاعدة البيانات لدعم اللغة العربية والإنجليزية.

تُستخدم قاعدة البيانات لإدارة المنتجات والتصنيفات والعملاء والموردين والمبيعات والمشتريات والمدفوعات والمرتجعات وحركات المخزون والمستخدمين والصلاحيات وإعدادات المتجر.

## 2. القواعد العامة لتصميم قاعدة البيانات

1. استخدام `BIGINT UNSIGNED` للمعرفات الأساسية.
2. استخدام `DECIMAL(12,2)` للأسعار والمبالغ المالية.
3. استخدام `DECIMAL(12,3)` للكميات.
4. استخدام `DATETIME` لتواريخ العمليات التي تحتاج إلى وقت محدد.
5. استخدام `TIMESTAMP` لحقول الإنشاء والتحديث.
6. استخدام المفاتيح الأساسية والخارجية لربط الجداول.
7. استخدام الفهارس لتحسين سرعة الاستعلامات.
8. استخدام `UNIQUE` لمنع تكرار القيم التي يجب أن تكون فريدة.
9. تخزين كلمات المرور بصيغة Hash داخل `password_hash`.
10. الاحتفاظ بسجلات العمليات المالية والمخزنية وعدم حذف الفواتير المؤكدة حذفاً نهائياً.

## 3. الجداول وحقولها

### 3.1 جدول الأدوار (roles)

يخزن أدوار المستخدمين داخل النظام.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| name | VARCHAR(50) | NOT NULL, UNIQUE |
| description | VARCHAR(255) | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.2 جدول المستخدمين (users)

يخزن حسابات المستخدمين وبيانات الدخول وحالة الحساب.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| role_id | BIGINT UNSIGNED | FK, NOT NULL |
| username | VARCHAR(100) | NOT NULL, UNIQUE |
| full_name | VARCHAR(150) | NOT NULL |
| email | VARCHAR(150) | NULL, UNIQUE |
| password_hash | VARCHAR(255) | NOT NULL |
| is_active | TINYINT(1) | NOT NULL, DEFAULT 1 |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP |

### 3.3 جدول التصنيفات (categories)

يخزن تصنيفات المنتجات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| name | VARCHAR(120) | NOT NULL, UNIQUE |
| description | TEXT | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.4 جدول المنتجات (products)

يخزن بيانات المنتجات وأسعارها وكمياتها الحالية.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| category_id | BIGINT UNSIGNED | FK, NULL |
| sku | VARCHAR(100) | NOT NULL, UNIQUE |
| barcode | VARCHAR(100) | NULL, UNIQUE |
| name | VARCHAR(180) | NOT NULL |
| description | TEXT | NULL |
| purchase_price | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| selling_price | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| current_stock | DECIMAL(12,3) | NOT NULL, DEFAULT 0.000 |
| reorder_level | DECIMAL(12,3) | NOT NULL, DEFAULT 0.000 |
| is_active | TINYINT(1) | NOT NULL, DEFAULT 1 |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP |

### 3.5 جدول العملاء (customers)

يخزن بيانات العملاء.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| name | VARCHAR(150) | NOT NULL |
| phone | VARCHAR(30) | NULL |
| email | VARCHAR(150) | NULL |
| address | TEXT | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.6 جدول الموردين (suppliers)

يخزن بيانات الموردين.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| name | VARCHAR(150) | NOT NULL |
| phone | VARCHAR(30) | NULL |
| email | VARCHAR(150) | NULL |
| address | TEXT | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.7 جدول المبيعات (sales)

يخزن فواتير المبيعات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| invoice_number | VARCHAR(50) | NOT NULL, UNIQUE |
| customer_id | BIGINT UNSIGNED | FK, NULL |
| user_id | BIGINT UNSIGNED | FK, NOT NULL |
| sale_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| subtotal | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| discount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| total_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| paid_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| status | ENUM('draft','confirmed','cancelled') | NOT NULL, DEFAULT 'draft' |
| notes | TEXT | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.8 جدول تفاصيل المبيعات (sale_items)

يخزن المنتجات والكميات والأسعار والتكاليف المرتبطة بكل فاتورة بيع.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| sale_id | BIGINT UNSIGNED | FK, NOT NULL |
| product_id | BIGINT UNSIGNED | FK, NOT NULL |
| quantity | DECIMAL(12,3) | NOT NULL |
| unit_price | DECIMAL(12,2) | NOT NULL |
| unit_cost | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| discount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| total | DECIMAL(12,2) | NOT NULL |

### 3.9 جدول مدفوعات المبيعات (sale_payments)

يخزن دفعات فواتير المبيعات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| sale_id | BIGINT UNSIGNED | FK, NOT NULL |
| amount | DECIMAL(12,2) | NOT NULL |
| payment_method | ENUM('cash','card','bank_transfer','other') | NOT NULL, DEFAULT 'cash' |
| payment_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| notes | VARCHAR(255) | NULL |

### 3.10 جدول المشتريات (purchases)

يخزن فواتير شراء المنتجات من الموردين.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| invoice_number | VARCHAR(50) | NOT NULL, UNIQUE |
| supplier_id | BIGINT UNSIGNED | FK, NOT NULL |
| user_id | BIGINT UNSIGNED | FK, NOT NULL |
| purchase_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| subtotal | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| discount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| total_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| paid_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| status | ENUM('draft','received','cancelled') | NOT NULL, DEFAULT 'draft' |
| notes | TEXT | NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.11 جدول تفاصيل المشتريات (purchase_items)

يخزن المنتجات والكميات وتكاليف الشراء في كل فاتورة مشتريات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| purchase_id | BIGINT UNSIGNED | FK, NOT NULL |
| product_id | BIGINT UNSIGNED | FK, NOT NULL |
| quantity | DECIMAL(12,3) | NOT NULL |
| unit_cost | DECIMAL(12,2) | NOT NULL |
| total | DECIMAL(12,2) | NOT NULL |

### 3.12 جدول مدفوعات المشتريات (purchase_payments)

يخزن الدفعات المالية المرتبطة بفواتير المشتريات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| purchase_id | BIGINT UNSIGNED | FK, NOT NULL |
| amount | DECIMAL(12,2) | NOT NULL |
| payment_method | ENUM('cash','card','bank_transfer','other') | NOT NULL, DEFAULT 'cash' |
| payment_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| notes | VARCHAR(255) | NULL |

### 3.13 جدول حركات المخزون (inventory_movements)

يسجل الحركات التي تؤثر في مخزون المنتجات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| product_id | BIGINT UNSIGNED | FK, NOT NULL |
| user_id | BIGINT UNSIGNED | FK, NOT NULL |
| movement_type | ENUM('purchase','sale','sales_return','purchase_return','adjustment') | NOT NULL |
| reference_type | VARCHAR(50) | NULL |
| reference_id | BIGINT UNSIGNED | NULL |
| quantity | DECIMAL(12,3) | NOT NULL |
| unit_cost | DECIMAL(12,2) | NULL, DEFAULT 0.00 |
| movement_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| notes | TEXT | NULL |

### 3.14 جدول مرتجعات المبيعات (sales_returns)

يخزن عمليات إرجاع المنتجات المرتبطة بفواتير المبيعات.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| return_number | VARCHAR(50) | NOT NULL, UNIQUE |
| sale_id | BIGINT UNSIGNED | FK, NOT NULL |
| user_id | BIGINT UNSIGNED | FK, NOT NULL |
| return_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| total_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| reason | TEXT | NULL |
| status | ENUM('draft','confirmed','cancelled') | NOT NULL, DEFAULT 'draft' |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.15 جدول تفاصيل مرتجعات المبيعات (sales_return_items)

يخزن المنتجات والكميات المرتجعة من فواتير المبيعات، مع تحديد حالة المنتج.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| sales_return_id | BIGINT UNSIGNED | FK, NOT NULL |
| sale_item_id | BIGINT UNSIGNED | FK, NOT NULL |
| product_id | BIGINT UNSIGNED | FK, NOT NULL |
| quantity | DECIMAL(12,3) | NOT NULL |
| unit_price | DECIMAL(12,2) | NOT NULL |
| total | DECIMAL(12,2) | NOT NULL |
| condition_status | ENUM('resellable','damaged') | NOT NULL, DEFAULT 'resellable' |

### 3.16 جدول مرتجعات المشتريات (purchase_returns)

يخزن عمليات إرجاع المنتجات إلى الموردين.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| return_number | VARCHAR(50) | NOT NULL, UNIQUE |
| purchase_id | BIGINT UNSIGNED | FK, NOT NULL |
| user_id | BIGINT UNSIGNED | FK, NOT NULL |
| return_date | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| total_amount | DECIMAL(12,2) | NOT NULL, DEFAULT 0.00 |
| reason | TEXT | NULL |
| status | ENUM('draft','confirmed','cancelled') | NOT NULL, DEFAULT 'draft' |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

### 3.17 جدول تفاصيل مرتجعات المشتريات (purchase_return_items)

يخزن المنتجات والكميات المرتجعة إلى الموردين.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| purchase_return_id | BIGINT UNSIGNED | FK, NOT NULL |
| purchase_item_id | BIGINT UNSIGNED | FK, NOT NULL |
| product_id | BIGINT UNSIGNED | FK, NOT NULL |
| quantity | DECIMAL(12,3) | NOT NULL |
| unit_cost | DECIMAL(12,2) | NOT NULL |
| total | DECIMAL(12,2) | NOT NULL |

### 3.18 جدول إعدادات المتجر (store_settings)

يخزن إعدادات المتجر الأساسية.

| الحقل | النوع | القيود |
|---|---|---|
| id | BIGINT UNSIGNED | PK, AUTO_INCREMENT |
| store_name | VARCHAR(180) | NOT NULL |
| phone | VARCHAR(30) | NULL |
| address | TEXT | NULL |
| currency_code | VARCHAR(10) | NOT NULL, DEFAULT 'USD' |
| language | VARCHAR(5) | NOT NULL, DEFAULT 'ar' |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |
| updated_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP, ON UPDATE CURRENT_TIMESTAMP |

## 4. العلاقات بين الجداول

تُستخدم المفاتيح الخارجية التالية لربط الجداول:

| الجدول | الحقل | الجدول المرتبط | الحقل المرتبط |
|---|---|---|---|
| users | role_id | roles | id |
| products | category_id | categories | id |
| sales | customer_id | customers | id |
| sales | user_id | users | id |
| purchases | supplier_id | suppliers | id |
| purchases | user_id | users | id |
| sale_items | sale_id | sales | id |
| sale_items | product_id | products | id |
| sale_payments | sale_id | sales | id |
| purchase_items | purchase_id | purchases | id |
| purchase_items | product_id | products | id |
| purchase_payments | purchase_id | purchases | id |
| inventory_movements | product_id | products | id |
| inventory_movements | user_id | users | id |
| sales_returns | sale_id | sales | id |
| sales_returns | user_id | users | id |
| sales_return_items | sales_return_id | sales_returns | id |
| sales_return_items | sale_item_id | sale_items | id |
| sales_return_items | product_id | products | id |
| purchase_returns | purchase_id | purchases | id |
| purchase_returns | user_id | users | id |
| purchase_return_items | purchase_return_id | purchase_returns | id |
| purchase_return_items | purchase_item_id | purchase_items | id |
| purchase_return_items | product_id | products | id |

### 4.1 العلاقات الرئيسية

- الأدوار والمستخدمون: علاقة واحد إلى متعدد.
- التصنيفات والمنتجات: علاقة واحد إلى متعدد.
- العملاء والمبيعات: علاقة واحد إلى متعدد، مع إمكانية إنشاء فاتورة دون عميل.
- الموردون والمشتريات: علاقة واحد إلى متعدد.
- المستخدمون والمبيعات: علاقة واحد إلى متعدد.
- المستخدمون والمشتريات: علاقة واحد إلى متعدد.
- المبيعات وتفاصيل المبيعات: علاقة واحد إلى متعدد.
- المشتريات وتفاصيل المشتريات: علاقة واحد إلى متعدد.
- الفواتير والمدفوعات: علاقة واحد إلى متعدد.
- المنتجات وحركات المخزون: علاقة واحد إلى متعدد.
- فواتير المبيعات ومرتجعات المبيعات: علاقة واحد إلى متعدد.
- فواتير المشتريات ومرتجعات المشتريات: علاقة واحد إلى متعدد.
- المرتجعات وتفاصيل المرتجعات: علاقة واحد إلى متعدد.

## 5. الفهارس والقيود الموجودة

وفقاً لبنية الجداول المستخرجة من MySQL:

### 5.1 المفاتيح الأساسية

لكل جدول حقل `id` من النوع `BIGINT UNSIGNED`، وهو مفتاح أساسي مع `AUTO_INCREMENT`.

### 5.2 القيود الفريدة UNIQUE

- `roles.name`
- `users.username`
- `users.email`
- `categories.name`
- `products.sku`
- `products.barcode`
- `sales.invoice_number`
- `purchases.invoice_number`
- `sales_returns.return_number`
- `purchase_returns.return_number`

### 5.3 المفاتيح الخارجية

تُستخدم المفاتيح الخارجية المذكورة في قسم العلاقات لضمان سلامة الربط بين السجلات.

### 5.4 الفهارس العادية

توجد فهارس على عدد من حقول الربط والبحث، مثل معرفات المستخدمين والمنتجات والعملاء والموردين وتواريخ الفواتير وحالاتها.

## 6. قواعد العمل وسلامة البيانات

هذا القسم يصف السلوك المطلوب من النظام، وليس بالضرورة قيوداً مفروضة حالياً بواسطة MySQL. يجب تنفيذ القواعد التي لا تفرضها قاعدة البيانات في Backend والتحقق منها قبل حفظ العمليات.

### 6.1 إدارة المنتجات

1. يجب أن يكون SKU فريداً.
2. يجب منع إدخال أسعار أو كميات سالبة في العمليات العادية.
3. يجب تحديث `current_stock` عند تنفيذ الحركات المخزنية المعتمدة.
4. يجب استخدام `reorder_level` لتحديد المنتجات التي وصلت إلى حد إعادة الطلب.
5. يجب استخدام `is_active` لتعطيل المنتج بدلاً من حذفه عند ارتباطه بعمليات سابقة.

### 6.2 المبيعات

1. يجب أن يكون رقم الفاتورة فريداً.
2. يجب التحقق من توفر الكمية قبل تأكيد البيع.
3. يجب منع بيع كمية تتجاوز المخزون المتاح.
4. يجب حساب الإجمالي والخصومات والمدفوعات في Backend.
5. يجب تسجيل تكلفة المنتج وقت البيع في `sale_items.unit_cost`.
6. لا يُسمح بتعديل فاتورة مؤكدة بطريقة تؤثر في السجل المالي أو المخزني دون إجراء معالجة واضحة.

### 6.3 المشتريات

1. يجب ربط فاتورة الشراء بمورد ومستخدم.
2. لا تزيد كمية المخزون بمجرد إنشاء فاتورة مسودة.
3. تتم زيادة المخزون عند استلام المشتريات وتأكيد العملية.
4. يجب تسجيل حركة مخزون مرتبطة بعملية الاستلام.
5. يجب تحديث تكلفة المنتج وفق سياسة التكلفة التي يعتمدها النظام.

### 6.4 المدفوعات

1. يجب أن تكون قيمة الدفعة موجبة.
2. يجب التحقق من عدم تجاوز مجموع المدفوعات للمبلغ المستحق.
3. يجب حساب الرصيد المتبقي في Backend؛ لأن حقول `due_amount` غير موجودة حالياً في جداول الفواتير.
4. يجب تسجيل طريقة الدفع وتاريخها.
5. يمكن أن تحتوي الفاتورة على أكثر من دفعة.

### 6.5 المرتجعات

1. يجب ربط مرتجع البيع بفاتورة البيع الأصلية.
2. يجب ربط تفاصيل مرتجع البيع ببند البيع الأصلي.
3. يجب منع إرجاع كمية تتجاوز الكمية المباعة بعد احتساب المرتجعات السابقة.
4. يجب زيادة المخزون عند اعتماد مرتجع بيع لمنتج صالح لإعادة البيع.
5. يجب عدم زيادة المخزون للمنتج التالف.
6. يجب منع إرجاع كمية إلى المورد تتجاوز الكمية المستلمة بعد احتساب المرتجعات السابقة.
7. يجب تسجيل حركة مخزون عند اعتماد المرتجعات التي تؤثر في المخزون.

### 6.6 حركات المخزون

1. يجب تسجيل كل حركة تؤثر في كمية المنتج.
2. أنواع الحركات المسجلة في `movement_type` هي:
   - `purchase`
   - `sale`
   - `sales_return`
   - `purchase_return`
   - `adjustment`
3. يُستخدم `reference_type` و`reference_id` لربط الحركة بالعملية المرتبطة بها.
4. يجب تنفيذ تحديث المخزون وتسجيل الحركة ضمن Transaction واحدة.
5. يجب منع تسجيل الحركة نفسها أكثر من مرة عند إعادة إرسال طلب العملية.

### 6.7 المعاملات Transactions

يجب استخدام المعاملات في العمليات التي تؤثر في أكثر من جدول، وبالأخص:

- تأكيد فاتورة البيع وتحديث المخزون وتسجيل الحركة.
- استلام المشتريات وتحديث المخزون وتسجيل الحركة.
- اعتماد المرتجعات وتحديث المخزون.
- تسجيل الدفعات وتحديث الحسابات المرتبطة بها.

في حال فشل أي جزء من العملية يجب التراجع عن جميع التغييرات المرتبطة بها.

## 7. ملاحظات مهمة حول البنية الحالية

1. جدول المنتجات يستخدم `name` بدلاً من فصل الاسم العربي والإنجليزي.
2. جدول التصنيفات يستخدم `name` بدلاً من `name_ar` و`name_en`.
3. حالة المستخدم والمنتج ممثلة بالحقل `is_active` من النوع `TINYINT(1)`.
4. جداول العملاء والموردين لا تحتوي حالياً على حقل حالة.
5. جدول المبيعات يستخدم `sale_date`.
6. جدول المشتريات يستخدم `purchase_date`.
7. جداول المبيعات والمشتريات لا تحتوي حالياً على حقل `due_amount` أو `payment_status`.
8. جدول تفاصيل المبيعات يستخدم `total` بدلاً من `line_total`.
9. جدول تفاصيل المشتريات يحتوي على `total` ولا يحتوي على حقل `discount`.
10. جداول المدفوعات لا تحتوي حالياً على `user_id`.
11. طريقة التحويل البنكي ممثلة بالقيمة `bank_transfer`.
12. جدول حركات المخزون يستخدم `quantity` و`reference_type`، ولا يحتوي على حقول منفصلة باسم `quantity_in` و`quantity_out` و`balance_after`.
13. جدول مرتجعات المبيعات يستخدم `reason` و`status` بالقيم `draft` و`confirmed` و`cancelled`.
14. تفاصيل مرتجعات المبيعات تستخدم `condition_status` بالقيم `resellable` و`damaged`.
15. جدول مرتجعات المشتريات يستخدم `reason` و`status` بالقيم `draft` و`confirmed` و`cancelled`.
16. جدول إعدادات المتجر يستخدم `store_name` و`language`، ولا يحتوي على حقول منفصلة لاسم المتجر بالعربية والإنجليزية.
17. جدول إعدادات المتجر لا يحتوي حالياً على حقل البريد الإلكتروني.
18. لا توجد حالياً جداول مستقلة للفروع أو المستودعات؛ الإصدار الحالي يستهدف متجراً واحداً ومستودعاً واحداً.

## 8. نطاق قاعدة البيانات في الإصدار الأول

تدعم قاعدة البيانات الحالية:

- إدارة المستخدمين والأدوار.
- إدارة المنتجات والتصنيفات.
- إدارة العملاء والموردين.
- إدارة فواتير المبيعات وتفاصيلها.
- إدارة فواتير المشتريات وتفاصيلها.
- إدارة مدفوعات المبيعات والمشتريات.
- إدارة مرتجعات المبيعات والمشتريات.
- تسجيل حركات المخزون.
- تخزين إعدادات المتجر والعملة واللغة.

ولا تشمل البنية الحالية:

- تعدد الفروع.
- تعدد المستودعات.
- إدارة العملات المتعددة داخل الفاتورة الواحدة.
- نظام محاسبي متكامل.

## 9. الخلاصة

تتكون قاعدة بيانات نظام إدارة المبيعات والمخزون من 18 جدولاً مترابطاً باستخدام المفاتيح الأساسية والخارجية.

تغطي هذه الجداول الوظائف الأساسية المطلوبة لإدارة المنتجات والمخزون والمبيعات والمشتريات والمدفوعات والمرتجعات والمستخدمين.

تعتمد هذه الوثيقة على بنية قاعدة البيانات الفعلية المستخرجة من MySQL، بينما تُنفّذ قواعد العمل والتحقق من العمليات والحسابات في Backend عند الحاجة.

