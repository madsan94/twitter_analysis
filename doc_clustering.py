from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

document=['PPatel Chhattisgarh government finalise fresh order rapid test kits today https ytzkroCKOv Here Chattis', 'PPatel This reality What congress done Years what modi done https gkOipwQKHQ', 'ndtvindia Coronavirus https', 'VijayIsMyLife They accuse others with what they here link article Hindu Good', 'ShashiTharoor sardesairajdeep RahulGandhi question INCIndia cells natural that they show bias', 'Naim ABPNews RubikaLiyaquat TAUFIQ RAZA HalimAkhtar mohd Irfana Azzuwrites https AWyWkewV', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'Bharatvarsh Live Debate Leader Nalin Kohli Defends Modi over Rahul Gandhi Comment Covid Test https siluwa', 'realDonaldTrump Chrismc patton prayingmedic Dark light Qanon Photo Surfaces Chief Meeting https MJATGw', 'AMIT GUJJU band', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'ashoswai Getting testing kits from China What happened Ramdev Patanjali Where Modi Make India https ovGg', 'iamsrk Salman doesn have Salman doesn take supports political parties Salman doesn promote charity Salm','MahantBalaknath bjpkm kisan ombirlakota stIndiaNews KailashBaytu https rgJR', 'Mahrukh Modi terrorist want Kashmir Khalistan TeamISPOfficial TeamForPakistan DrHamzaO', 'Deepakkhatri have come know that Rahul Gandhi visionary leader Narendra Modi television leader Godi medi', 'IshitaJ Ghoragyani Good Subhash GuddiSheetal gudiyamishra Gullu XwwmPVkTobMn https KJLhJTtUhk', 'PPatel Chhattisgarh government finalise fresh order rapid test kits today https ytzkroCKOv Here Chattis', 'Islamik loggg India Hindu marnee lagaaa haaa Boloooo Boloooo bolo india https sbQvo', 'iamsrk Salman doesn have Salman doesn take supports political parties Salman doesn promote charity Salm', 'ShiningSadaf missed that rose favor forced conversion Hindu girl Bannu equipped financed Hitler through', 'indiantweeter hounding acid attack survivor because liked leftists while twitter never suspends people spreading', 'iamWajahat AMIT GUJJU video humkaa poora chaahiye', 'NagpurKaRajini Twitter courage suspend most uncouth venom spewing anti Hindu bigot ranaayyub handle', 'CricBollyBuzz VIDEO This video Sita Dipika Chikhlia with young Modi winning Internet', 'Sneha Stupid only thisRespect Equal Hindu Muslim Christian https ychmIq', 'Mahrukh Modi killer murderer TeamISPOfficial TeamForPakistan DrHamzaOfficial https', 'Infinitchy Twitter suspend people giving their exasperation will they suspend those their Indian employees', 'samjawed time when hospitals busy fighting COVID Indian right wingers playing pranks AlZahra AlAin', 'PMBhutan Lyonchhen speaks with narendramodi Prime Minister India Shri Narendra Modi called Lyonchhen Lotay Tshering this', 'Isko Sana Acchi wali Bhejna Chachta Bhej sakta https ouupsZWNZx', 'soulalive aajtak Muslims', 'Jihaadis double meaning freedom Speech community call Jihaad nothing Holy against evil', 'KashmiriPandit Year India Indira Gandhi Sheikh Abdullah Names villages Kashmir changed from', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'AsYouNotWish Jagmohan responsible Kashmiri Pandit exodus Indira responsible Sikh radicalisation responsibl', 'KanchanGupta will ensure that less unfortunate among Hindu refugees from Muslim majority', 'alnassar Muslim countries Indians where most them Hindu treated with humanity respect Muslims trea', 'gave right mimcery about Hindu Goddesses Does anyone does mimcery about Prophet https DxabiUgIJE', 'AsYouNotWish Hindu comedians make Muslims then Lots laugh about with those wild animal bree https iuycfWyyHk', 'News workers providing food crore needy people daily Party president Nadda', 'RajeevRai https HYxg bomco', 'viral Hindu', 'RoshanSdrprop Revant Singh Hindu murdered Muslim neighbors bcoz Supported Modiji call clap honour health workers', 'NetajiBond Meet Sana Shaik Muslamaan Billi from Mumbai rabid Hindu hater lives Hindu majority country spew venom', 'MohanTh Kabir Coming Humanity Will Religion World Hindu Muslim will become will fight', 'kunjam sood ipardeep', 'iAdilxxx SRKians dushmani lene liye aukat hona zaroori amit gujju nahi https', 'sabanaqvi many moulavis dictated that business with Hindu vendors', 'AsYouNotWish question Muhammad meet fate Kamlesh Tiwari crack filthy insensitive jokes Hindu deities', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'thakkar sameet Once MODI announced aroonpurie Kumar Birla changed their position seeing changing direction wind During', 'Dikshapandey', 'MdZaid hire more doctors immediately instead discussing hindu muslisms need hour https ujxINvFPxJ', 'ShruvRahul AMIT GUJJU crisy tere andar hain religion respect krta hain festival manta celebrate', 'GaneshJaiHind Sonia World Richest Politician Tours days year outside India Priyanka stays', 'https FHes ACYz https BUQpD', 'Mahrukh Their allied party government which taking citizenship indian minority group', 'Sujay Narendra Modi Taking These Decisions Alone being Advised Best Scientific Medical minds Shehzad', 'PiyushSingh Great step VinodumishraYou Chairman Malad Shakari Bank Deputy leader Municipal cooperation', 'iHrithik Mania Dear Hrithikians Rangoli against tweets Like karne pahle dekhe Tweet kiske There lots peopl', 'narendramodi First last Live Press Conference Journalist boldly asked killed Justice Loya httpstZQGuzqaNv', 'BHIMSIN', 'ashoswai Getting testing kits from China What happened Ramdev Patanjali Where Modi Make India https ovGg', 'IshitaJ BivashPrasadS pradip BrijSharma Chandan ColorsiTV coolamitkr Cutepie Damini https dkvlSyPK', 'sujataanandan know RahulGandhi realised perhaps without knowing made Maamu Narendra Modi today', 'HUNTER SINGH AMIT GUJJU Waah modi waah Hypocrisy seema hoti https rucdvbuPs', 'SRKsFARHA AMIT GUJJU want', 'Team case Rangoli Suspended Twitter Followers Blue tick', 'KashmiriPandit Year India Indira Gandhi Sheikh Abdullah Names villages Kashmir changed from', 'DrJawahars know that Resident Doctor Hindu Hospital Delhi been terminated https HOei', 'IndianPrism have nothing against Muslims still support calls genocide against them choose lecture Musli', 'najibjer kata personal project Kalau full stock takde modi saya pilih', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'kazi Modi liar follower Adolf Hitler murdered thousands Jews Modi agenda Adolf', 'jigneshmevani Hindu Rastra', 'Jihaadis double meaning freedom Speech community call Jihaad nothing Holy against evil', 'Mahrukh Modi become India announced discriminatory citizenship laws targeting Muslims', 'Anamikabarman absolutely right', 'That FluffyGuy AMIT GUJJU Apni ghatiya soch badal https yKTakhnno', 'CLLFBI', 'OpIndia Indian government slammed Commission International Religious Freedom USCIRF falsely criticising countr', 'Modi Godi media band karo', 'Raghuna Glory Ancestors More than just architectural feat century Prambanan Temple mystical', 'AsYouNotWish Watch Munawar Faruqui making dead Hindu pilgrim victims Godhra train burning blaming Amit Shah', 'hindu ImpExpSMENews India Spices Board https MkhWAY', 'Mahrukh Indian Prime Minister Modi member group when Modi became Chief Minis', 'rajsingh Hindu Lady', 'Just reminder carelessPakistanis people going unleash massive attack before', 'AsYouNotWish Jagmohan responsible Kashmiri Pandit exodus Indira responsible Sikh radicalisation responsibl', 'ashoswai Looks biased article your disclaimer Practising temple going Hindu have great frds https yYttzYV', 'iamvijay AMIT GUJJU part India respects religions That enough prove love country', 'pyari bacchi pyari bacchi Hindu putra rudera prtap YourAmitTeamBDS HiteshNandavane Gayatri Swarajoshi', 'OpIndia Indian government slammed Commission International Religious Freedom USCIRF falsely criticising countr', 'rkhuria Modi hold Press Conference give interview poodles including Akshay Kumar', 'phani Judges appointed President filed party these morons have guts criticize', 'nisheethsharan Please help with following info blog Name Hindu spat cops Name city where', 'aajtak https BcwuXg', 'VijayIsMyLife They accuse others with what they here link article Hindu Good', 'hindu rvaidya Nobody asking support what comes unasked regulatory tape Indian mentality https uxpoZOdAx']
vectorizer = TfidfVectorizer(analyzer="word",stop_words='english')
X = vectorizer.fit_transform(document)

print(X.shape)
print(type(X))
print(X[0])
print(X[1])
print(X[1],X[0])
print(len(vectorizer.get_feature_names()))
true_k = 2
model = KMeans(n_clusters=true_k,init='k-means++',max_iter=1000,n_init=1)
model.fit(X)

# order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
print(model.labels_)
# print(document[0])
# print(document[1])
print(model.cluster_centers_.shape)

# order_centroids = model.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()

"""
for i in range(true_k):
    print("Cluster %d:" %i)
    for ind in order_centroids[i, :10]:
        print( '%s' % terms[ind])

print("\n")
print("Prediction")
X = vectorizer.transform(["Prashant Kishor, a close aide of Bihar Chief Minister Nitish Kumar, today drew fresh battlelines with ally BJP, tweeting that there would be no implementation of the citizenship law or list in the state. To compound it, he also thanked Congress's Rahul Gandhi and his sister, Priyanka Gandhi Vadra, for their formal and unequivocal rejection of #CAA..."])
predicted = model.predict(X)
print(predicted)
"""