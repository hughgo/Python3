import tkinter
win = tkinter.Tk()
win.title("qianxiao")
#win.geometry("400x400+800+400")

'''
文本控件，用于显示多行文本
'''
#创建滚动条
scroll = tkinter.Scrollbar()
#height:显示的行数
text = tkinter.Text(win,width =50,height = 10)
#side 放到窗体的哪一侧
scroll.pack(side  =tkinter.RIGHT,fill = tkinter.Y)
text.pack(side  =tkinter.RIGHT,fill = tkinter.Y)
#关联
scroll.config(command =text.yview)
text.config(yscrollcommand =scroll.set)

str = '''2016-12-31 Weekly Address - Working Together to Keep America Moving Forward
2016-12-17 Weekly Address - Ensuring a Fair and Competitive Marketplace
2016-12-10 Weekly Address - It's Time to Get Covered on the Health Insurance Marketplace
2016-12-03 Weekly Address - Pass the 21st Century Cures Act
2016-11-24 Weekly Address - Coming Together On Thanksgiving
2016-11-19 Weekly Address - Building on a Record of Economic Progress
2016-11-12 Weekly Address - Honoring Our Veterans
2016-11-05 Weekly Address - The Progress We've Made Because of the Affordable Care Act
2016-10-29 Weekly Address - Achieving the Mission of the Cancer Moonshot
2016-10-22 Weekly Address - Taking Action to Spur Competition in the Airline Industry and Give Consumers the Information They Need
2016-10-15 Weekly Address - Ensuring America Leads the World Into the Next Frontier
2016-10-08 Weekly Address - Continuing to Strengthen the Middle Class
2016-09-24 Weekly Address - Celebrating the National Museum of African American History and Culture
2016-09-17 Weekly Address - It’s Time for Republicans in Congress To Do Their Jobs
2016-09-10 Weekly Address - Upholding the Legacy of Those We Lost on September 11th
2016-09-03 Weekly Address - Building Upon the Legacy of Labor Day
2016-08-27 Weekly Address - Taking Action Against the Zika Virus
2016-08-20 Weekly Address - Celebrating the 100th Anniversary of the National Park Service
2016-08-13 Weekly Address - Providing a Better, Cleaner, Safer Future for Our Children
2016-08-06 Weekly Address - Representing the Best of America in the Summer Olympics
2016-07-30 Weekly Address - It’s Time to Fill the Vacancy on the Supreme Court
2016-07-23 Weekly Address - Protecting the Progress We’ve Made with Wall Street Reform
2016-07-16 Weekly Address - Coming Together to Find Solutions
2016-07-09 Weekly Address - Standing Together to Stop the Violence
2016-07-02 Weekly Address - Serving our Military Families This Fourth of July
2016-06-25 Weekly Address - Designating Stonewall National Monument
2016-06-18 Weekly Address - Standing with Orlando
2016-06-11 Weekly Address - Addressing Puerto Rico's Economic Crisis
2016-06-04 Weekly Address - Building on America's Economic Recovery
2016-05-28 Weekly Address - Remembering Our Fallen Heroes
2016-05-21 Weekly Address - Expanding Overtime Pay
2016-05-14 Weekly Address - A Conversation About Addiction
2016-05-07 Weekly Address - Happy Mother's Day From President Obama
2016-04-30 Weekly Address - It's Time for the Senate To Do Its Job
2016-04-23 Weekly Address - Building a Fairer and More Effective Criminal Justice System
2016-04-09 Weekly Address - Playing by the Same Rules
2016-04-02 Weekly Address - Securing the World from Nuclear Terrorism
2016-03-26 Weekly Address - Defeating ISIL
2016-03-19 Weekly Address - President Obama’s Supreme Court Nomination
2016-03-12 Weekly Address - The Legacy of Nancy Reagan
2016-03-05 Weekly Address - The American Spirit of Innovation
2016-02-27 Weekly Address - Degrading and Destroying ISIL
2016-02-20 Weekly Address - A New Chapter with Cuba
2016-02-13 Weekly Address - The State of American Politics
2016-02-06 Weekly Address - Doubling Our Clean Energy Funding to Address the Challenge of Climate Change
2016-01-30 Weekly Address - Giving Every Student an Opportunity to Learn Through Computer Science For All
2016-01-23 Weekly Address - Affordable Care Act is Making a Difference for Millions of Americans
2016-01-16 Weekly Address - Improving Economic Security by Strengthening and Modernizing the Unemployment Insurance System
2016-01-09 Weekly Address - America Can Do Anything
2016-01-01 Weekly Address - Making America Safer for Our Children
2015-12-25 Weekly Address - Merry Christmas from the President and First Lady
2015-12-19 Weekly Address - Top 10 Things that Happened in 2015
2015-12-12 Weekly Address - Standing Strong in the Face of Terrorism
2015-12-05 Weekly Address - We Will Not Be Terrorized
2015-11-26 Weekly Address - This Thanksgiving, Recognizing the Greatness of American Generosity
2015-11-21 Weekly Address - In the Face of Terror, We Stand as One
2015-11-14 Weekly Address - Giving Veterans their Chance
2015-11-07 Weekly Address - If You Haven't Gotten Covered, Now's Your Chance
2015-10-31 Weekly Address - It's Time To Reform our Criminal Justice System
2015-10-24 Weekly Address - Protecting our Planet for Future Generations
2015-10-17 Weekly Address - Working for Meaningful Criminal Justice Reform
2015-10-10 Weekly Address - Writing the Rules for a Global Economy
2015-10-03 Weekly Address - Congress Should Do its Job and Pass a Serious Budget
2015-09-26 Weekly Address - Dispose of Your Expired and Unwanted Prescription Drugs
2015-09-19 Weekly Address - It’s Time for Congress To Pass a Responsible Budget
2015-09-12 Weekly Address - A New College Scorecard
2015-09-05 Weekly Address - This Labor Day, Lets Talk About the Budget
2015-08-29 Weekly Address - Meeting the Global Threat of Climate Change
2015-08-22 Weekly Address - It's Time for Congress To Pass a Responsible Budget
2015-08-15 Weekly Address - Continuing Work to Improve Community Policing
2015-08-08 Weekly Address - Reaffirming Our Commitment to Protecting the Right to Vote
2015-08-01 Weekly Address - Celebrating Fifty Years of Medicare and Medicaid
2015-07-25 Weekly Address - Wall Street Reform is Working
2015-07-18 Weekly Address - A Comprehensive, Long-Term Deal with Iran
2015-07-11 Weekly Address - Making Our Communities Stronger through Fair Housing
2015-07-04 Weekly Address - Have a Safe and Happy Fourth of July
2015-06-27 Weekly Address - The Affordable Care Act is Here to Stay
2015-06-20 Weekly Address - Creating New Pathways of Opportunity for Americans Like You
2015-06-13 Weekly Address - Stand Up for American Workers and Pass TAA
2015-06-06 Weekly Address - Celebrating Immigrant Heritage Month'''
text.insert(tkinter.INSERT,str)
win.mainloop()