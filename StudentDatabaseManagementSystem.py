#!/usr/bin/env python
# coding: utf-8

# In[27]:


import sqlite3
from sqlite3 import Error
 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn


# In[28]:


def select_option1(conn):
    """
    1. The number of courses for which the student has registered
    """
    cur = conn.cursor()
    cur.execute("""select a.id, a.StudentName, count(*) as no_of_courses from Student a 
                inner join CourseRegistration b on a.ID=b.StudentID 
                inner join Courses c on b.CourseID=c.ID 
                group by b.StudentID;""")
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[29]:


def select_option2(conn):
    """
    2. The average marks of the students
    """
    cur = conn.cursor()
    cur.execute("""select a.id, a.StudentName, avg(Marks) as Average_Marks from Student a 
                inner join CourseRegistration b on a.ID=b.StudentID 
                inner join Courses c on b.CourseID=c.ID
                group by b.StudentID;""")
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[30]:


def select_option3(conn):
    """
    3. Which student scored the maximum marks for a course
    """
    cur = conn.cursor()
    print("""1. To see the student with maximum marks, Press 1
    \n2. To see the student with minimum marks, Press 2\n""")
    y = input('Enter 1 or 2:')
    
    if y == '1':
        cur.execute("""select a.id, a.StudentName, c.CourseName, max(Marks) as Highest_Marks from Student a 
                    inner join CourseRegistration b on a.ID=b.StudentID 
                    inner join Courses c on b.CourseID=c.ID
                    group by b.CourseID;""")
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
        
    elif y == '2':
        cur.execute("""select a.id, a.StudentName, c.CourseName, min(Marks) as Lowest_Marks from Student a 
                    inner join CourseRegistration b on a.ID=b.StudentID 
                    inner join Courses c on b.CourseID=c.ID
                    group by b.CourseID;""")
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
    
    else :
        print("""Sorry you have entered an incorrect number, nothing to display""")   


# In[31]:


def select_option4(conn):
    """
    4. The number of instructors present in a department
    """
    cur = conn.cursor()
    cur.execute("""select b.DeptName, count(*) as No_of_Instructors from Instructor a 
                inner join Department b on a.DeptID=b.ID 
                group by a.DeptID;""")
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[32]:


def select_option5(conn):
    """
    5. The courses for which the student registered
    """
    item = input('Enter Student Name:')
    cur = conn.cursor()
    print("\n5. Courses taken by"' '+item+'\n')
    cur.execute("""select a.ID,a.StudentName,c.CourseName from Student a 
                inner join CourseRegistration b on a.ID=b.StudentID 
                inner join Courses c on b.CourseID=c.ID
                inner join Department e on a.DeptID=e.ID
                where a.StudentName=?;""",[item])
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[33]:


def select_option6(conn):
    """
    6. The average marks for various courses
    """
    cur = conn.cursor()
    cur.execute("""select a.CourseName, avg(Marks) from Courses a 
                inner join CourseRegistration b on a.ID=b.CourseID 
                group by CourseID;""")
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[34]:


def select_option7(conn):
    """
    7. The number of part-time and full-time students, scholarship and non-scholarship students
    """
    cur = conn.cursor()
    print("""1. To see number of part-time and full-time students, Press 1
    \n2. To see number of scholarship and non-scholarship students, Press 2\n""")
    y = input('Enter 1 or 2: ')
    
    if y == '1':
        cur.execute("""select EnrollmentType, count(*) aS No_of_Students from Student group by EnrollmentType;""")
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
    elif y == '2':
        cur.execute("""select Scholarship, count(*) aS No_of_Students from Student group by Scholarship;""")
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
    else :
        print("""Sorry you have entered an incorrect number, nothing to display""")


# In[35]:


def select_option8(conn):
    """
    8. Fee details of a student
    """
    cur = conn.cursor()
    item2 = input('Enter Student Name: ')
    cur.execute("""select a.ID, StudentName, c.FeeDescrpition, b.Amount, AmountPaid, AmountDue from Student a
                inner join transactions b on a.ID=b.StudentID
                inner join Fees c on c.ID=b.FeeID
                where a.StudentName=?""",[item2])
 
    rows = cur.fetchall()
    cur.close()
    
    for row in rows:
        print(row)


# In[43]:


def select_option9(conn):
    """
    9. List of instructors and the courses they are teaching
    """
    cur = conn.cursor()
    cur.execute("""select InstructorName, CourseName from Instructor a 
                inner join Courses b on a.ID=b.InstructorID;""")
 
    rows = cur.fetchall()
    cur.close()
 
    for row in rows:
        print(row)


# In[37]:


def select_option10(conn):
    """
    10. Add courses to the database
    """
    cur = conn.cursor()
    CourseName = input('Please enter Course Name: ')
    Credits = input('Please enter Credits: ')
    Term = input('Please enter Term: ')
    InstructorID = input('Please enter InstructorID: ')
    DeptID = input('Please enter DeptID: ')
    sql_statement = """INSERT INTO Courses (CourseName, Credits, Term, InstructorID, DeptID) VALUES (?, ?, ?, ?, ?);"""
    cur.execute(sql_statement, (CourseName, Credits, Term, InstructorID, DeptID))
    conn.commit()
    cur.close()


# In[38]:


def select_option11(conn):
    """
    11. Update course credits
    """
    cur = conn.cursor()
    ID = input('Please enter ID: ')
    Credits = input('Please enter Credits: ')
    sql_statement = """Update Courses set Credits = ? where ID = ?;"""
    cur.execute(sql_statement, (Credits,ID))
    conn.commit()
    cur.close()


# In[39]:


def select_option12(conn):
    """
    12. Delete a course
    """
    cur = conn.cursor()
    item3 = input('Please Course Name: ')
    cur.execute("""delete from Courses where CourseName=?;""",[item3])
    conn.commit()
    cur.close()


# In[40]:


def main():
    database = r"C:\Users\17059\Desktop\Intro to databases\studentdb.db"
 
    # create a database connection
    conn = create_connection(database)
    
    with conn:
            
        while (True):
            print("""\nWelcome to the Student database application:
            1. To see number of courses for which students have registered,Press 1
            2. To see the average marks of the students, Press 2
            3. To see which students scored the maximum marks/minimum marks for a course, Press 3
            4. The number of instructors in each department, Press 4
            5. To see the courses for which a student registered, Press 5
            6. To see the average marks for various courses, Press 6
            7. To see number of Part-time and Full-time students, scholarship and non-scholarship students, Press 7
            8. To see fee details of a student, Press 8
            9. To see a the list of instructors and the courses taught by them, Press 9
            10. To add a course, Press 10
            11. To update course credits, Press 11
            12. To delete a course, Press 12
            Finally, to close application Press anything other than 1-12\n""")
            x = input('Enter a number:')
            if x == '1':
                print("\n1. The number of courses for which students have registered\n")
                select_option1(conn)
            
            elif x == '2':
                print("\n2. The average marks of the students\n")
                select_option2(conn)
                
            elif x == '3':
                print("\n3. Which student scored the maximum marks/minimum marks for a course\n")
                select_option3(conn)
    
            elif x == '4':
                print("\n4. The number of instructors in each department\n")
                select_option4(conn)
            
            elif x == '5':
                select_option5(conn)
            
            elif x == '6':
                print("\n6. The average marks for various courses\n")
                select_option6(conn)

            elif x == '7':
                print("\n7. Part-time and full-time students, scholarship and non-scholarship students\n")
                select_option7(conn)
                
            elif x == '8':
                print("\n8. Fee details of a student\n")
                select_option8(conn)
                
            elif x == '9':
                print("\n9. List of instructors and the courses they are teaching\n")
                select_option9(conn)
            
            elif x == '10':
                print("\n10. Insert a new course\n")
                select_option10(conn)
                
            elif x == '11':
                print("\n11. Update course credits\n")
                select_option11(conn)
            
            elif x == '12':
                print("\n12. Delete a course\n")
                select_option12(conn)
            
            else :
                print("\n Application Closed!!!!!\n")
                break
            
if __name__ == '__main__':
    main()
