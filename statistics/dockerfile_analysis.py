# -*- coding: utf-8 -*-
# @author puyangsky

import matplotlib.pyplot as plt

labels = 'Ubuntu', 'Centos', 'Alpine', 'RedHat', 'Debian', 'Fedora', 'Others'
fracs = [25, 20, 30, 10, 5, 6, 4]
explode = [0, 0.1, 0, 0, 0, 0, 0]  # 0.1 凸出这部分，
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
# autopct ，show percet
plt.pie(x=fracs, labels=labels, explode=explode, autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6
        )

plt.show()


