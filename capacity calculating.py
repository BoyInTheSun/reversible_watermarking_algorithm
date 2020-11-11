def capacity_calculating(img):
    # 转化为灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    width = len(img)
    height = len(img[0])
    frequency = list()
    # 计算灰度值的频率
    maxp = 0
    for i in range(256):
        frequency.append(0)
    for i in range(height):
        for j in range(width):
            frequency[img[i, j]] += 1
    for i in range(256):
        if (frequency[i] > frequency[maxp]):
            maxp = i
    #得到容量
    capacity = frequency[maxp]
    return capacity

def finding_max_and_min(img,img1):
    width = len(img)
    height = len(img[0])
    frequency = list()

    for i in range(256):
        ferquency.append(0)
    for i in range(height):
        for j in range(width):
            if(img1[i][j] == 0):
                frequency[img[i, j]] += 1

    maxp = 0
    min1 = 0
    min2 = 0
    for i in range(256):
        if (frequency[i] > frequency[maxp]):
            maxp = i
    if (maxp == 0):
        min = 1
    else:
        min = 0
    min1 = maxp - 1
    min2 = maxp + 1
    while(frequency[min1] != 0&&frequency[min2] !=0):
        if(frequency[min1] == 0):
            min = min1
        elif(frequency[min2] == 0):
            min = min2
        min1-=1
        min2-=1

    if (maxp < min):
        for i in range(height):
            for j in range(width):
                if (img1[i][j] == 0):
                    if (img[i, j] < min and img[i, j] > maxp):
                        img[i, j] += 1
    else:
        for i in range(height):
            for j in range(width):
                if (img1[i][j] == 0):
                    if (img[i, j] > min and img[i, j] < maxp):
                        img[i, j] -= 1

    bstring = reading()

    k = 0
    for i in range(height):
        for j in range(width):
            if (img1[i][j] == 0):
                if (img[i, j] == maxp and k < len(bstring)):
                    if (bstring[k] == '1' and min > maxp):
                        img[i, j] += 1
                    elif (bstring[k] == '1' and min < maxp):
                        img[i, j] -= 1
                    k += 1
            if k == len(bstring):
                break
        if k == len(bstring):
            break

def extracting_data(img,img1):
    width = len(img)
    height = len(img[0])
    frequency = list()

    for i in range(256):
        ferquency.append(0)
    for i in range(height):
        for j in range(width):
            if(img1[i][j] == 0):
                frequency[img[i][j]] += 1
    maxp = 0
    min1 = 0
    min2 = 0
    for i in range(256):
        if (frequency[i] > frequency[maxp]):
            maxp = i
    if (maxp == 0):
        min = 1
    else:
        min = 0
    min1 = maxp - 1
    min2 = maxp + 1
    while (frequency[min1] != 0 & & frequency[min2] != 0):
        if (frequency[min1] == 0):
            min = min1
        elif (frequency[min2] == 0):
            min = min2
        min1 -= 1
        min2 -= 1

    k = 0

    for i in range(height):
        for j in range(width):
            if (img1[i][j] == 0):
                if (img[i, j] == maxp):
                    k += 1
                    bstring[k] = '0'
                elif (img[i, j] == maxp - 1 and min < maxp):
                    k += 1
                    bstring[k] = '1'
                elif (pix[i, j] == maxp + 1 and self.min > self.maxp):
                    k += 1
                    bstring[k] = '1'

    if (maxp < min):
        for i in range(height):
            for j in range(width):
                if (img1[i][j] == 0):
                    if (img[i, j] <= min and img[i, j] > self.maxp):
                        img[i, j] -= 1
    else:
        for i in range(height):
            for j in range(width):
                if (img1[i][j] == 0):
                    if (img[i, j] >= min and img[i, j] < maxp):
                        img[i, j] += 1
    return bstring
def reading():
    input_image_path = ''
    file = os.path.splitext(input_image_path)
    filename, type = file
    print(type)

    if type in ['.png', '.jpg', '.jpeg']:
        size = 128
        dim = (size, size)
        img = cv2.imread(input_image_path)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        in_wm = np.array(img)
        bstring = ''
        for i in range(size):
            for j in range(size):
                if (in_wm[i][j]):
                    bstring += '1'
                else:
                    bstring += '0'
        return bstring

    elif type in ['.txt']:
        with open(input_image_path) as read_file:
            bstring = ''
            str = read_file.read()
            bstring = ''.join([bin(ord(c)).replace('0b', '') for c in str])
        return bstring

