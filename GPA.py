import tkinter as tk
from tkinter import ttk, messagebox

def calculate_gpa(score):
    """计算单科绩点（保留2位小数）"""
    gpa = max(score / 10 - 5, 0)
    return round(gpa, 2)

class GPACalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("沈阳工学院绩点计算器")
        self.root.geometry("600x450")
        self.courses = [] 
        self.create_widgets()
    
    def create_widgets(self):
        """构建所有UI组件"""
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10, padx=10, fill='x')
        
        ttk.Label(input_frame, text="课程名称:").grid(row=0, column=0, padx=5, sticky='e')
        self.course_entry = ttk.Entry(input_frame, width=20, font=('Arial', 12))
        self.course_entry.grid(row=0, column=1, padx=5)
        ttk.Label(input_frame, text="成绩 (0-100):").grid(row=0, column=2, padx=5, sticky='e')
        self.score_entry = ttk.Entry(input_frame, width=10, font=('Arial', 12))
        self.score_entry.grid(row=0, column=3, padx=5)
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)
        
        self.add_button = ttk.Button(button_frame, text="添加课程", command=self.add_course)
        self.add_button.pack(side='left', padx=5)
        
        self.calc_button = ttk.Button(button_frame, text="计算绩点", command=self.show_result)
        self.calc_button.pack(side='left', padx=5)
        
        self.clear_button = ttk.Button(button_frame, text="清空所有", command=self.clear_data)
        self.clear_button.pack(side='left', padx=5)
        
        self.tree = ttk.Treeview(
            self.root, 
            columns=('序号', '课程名称', '成绩', '绩点'), 
            show='headings',
            height=10
        )
        self.tree.heading('序号', text='序号')
        self.tree.heading('课程名称', text='课程名称')
        self.tree.heading('成绩', text='成绩')
        self.tree.heading('绩点', text='绩点')
        
        self.tree.column('序号', width=50, anchor='center')
        self.tree.column('课程名称', width=150, anchor='w')
        self.tree.column('成绩', width=80, anchor='center')
        self.tree.column('绩点', width=80, anchor='center')
        
        self.tree.pack(pady=10, padx=10, fill='both', expand=True)
        
        
        self.score_entry.bind('<Return>', lambda e: self.add_course())
    
    def add_course(self):
        """添加课程到列表"""
        course_name = self.course_entry.get().strip()
        score_input = self.score_entry.get().strip()
        
        if not course_name:
            messagebox.showerror("错误", "请输入课程名称！")
            return
        
        if not score_input:
            messagebox.showerror("错误", "请输入成绩！")
            return
        
        try:
            score = float(score_input)
            if not (0 <= score <= 100):
                messagebox.showerror("错误", "成绩必须在0到100之间！")
                return
            
           
            gpa = calculate_gpa(score)
            self.courses.append({
                'name': course_name,
                'score': score,
                'gpa': gpa
            })
            
           
            self.tree.insert(
                '', 
                'end', 
                values=(
                    len(self.courses),
                    course_name,
                    score,
                    gpa
                )
            )
            
            
            self.course_entry.delete(0, 'end')
            self.score_entry.delete(0, 'end')
            self.course_entry.focus()  
            
        except ValueError:
            messagebox.showerror("错误", "请输入有效的成绩数字！")
    
    def show_result(self):
        """显示计算结果"""
        if not self.courses:
            messagebox.showwarning("提示", "请先添加课程成绩！")
            return
        
        total_gpa = sum(course['gpa'] for course in self.courses)
        avg_gpa = total_gpa / len(self.courses)
        
        result_msg = (
            f"课程总数: {len(self.courses)}\n"
            f"总绩点: {round(total_gpa, 2)}\n"
            f"平均绩点: {round(avg_gpa, 2)}"
        )
        messagebox.showinfo("计算结果", result_msg)
    
    def clear_data(self):
        """清空所有数据"""
        self.courses.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    
    app = GPACalculatorApp(root)
    root.mainloop()