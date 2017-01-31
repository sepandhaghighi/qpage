import os
import datetime

IP_FINDER_API = "http://ipinfo.io/ip"
SERVER_API = "http://sepkjaer.pythonanywhere.com/install"
SOURCE_DIR = os.getcwd()  # Get Current Directory
RESOURCE_DIR = os.path.join(os.pardir, 'resource')
IMAGE_DIR = os.path.join(SOURCE_DIR, 'image')
DOC_DIR = os.path.join(SOURCE_DIR, 'doc')
OUT_DIR = os.path.join(SOURCE_DIR, 'output')
FONT_DIR = os.path.join(SOURCE_DIR, 'font')
SAMPLE_SITE_LIST=["http://www.qpage.ir/sample/sample-site1","http://www.qpage.ir/sample/sample-site2"]
SAMPLE_DICT_ADDR = {os.path.join(IMAGE_DIR, "profile.png"): "http://www.qpage.ir/sample/profile.png",
                    os.path.join(FONT_DIR, "font.TTF"): "http://www.qpage.ir/sample/font.TTF",
                    os.path.join(DOC_DIR, "resume.pdf"): "http://www.qpage.ir/sample/resume.pdf",
                    os.path.join(DOC_DIR, "resume.txt"): "http://www.qpage.ir/sample/resume.txt",
                    os.path.join(IMAGE_DIR, "icon.ico"): "http://www.qpage.ir/sample/icon.ico"}
SAMPLE_DICT_MESSAGE = ["Profile Image", "Font", "Resume Part-1", "Resume Part-2", "Icon File"]
BADGE_COLOR_LIST = ["brightgreen", "green", "yellowgreen", "yellow", "orange", "red", "lightgrey", "blue"]
IMAGE_COUNTER = 0
PDF_COUNTER = 0
SPACE = "&nbsp\n"

PAGE_NAME = ["Home"]  # list of default HOMEPAGE Name
ACTUAL_NAME = ["index"]  # List of Actual Name Like Home.Html
BREAK_LINE = "<hr/><hr/>\n"
HOMEPAGE = "http://www.qpage.ir"
VERSION = "2.0"
ADV_BADGE_STATIC = "https://img.shields.io/badge/"
ERROR_DICT = {"image_error": "[Error-1001]", "resume_error": "[Error-1002]", "firstpage_error": "[Error-1003]",
              "empty_error": "[Error-1004]"}
WARNING_DICT = {"icon_warning": "[Warning-2001]", "font_warning": "[Warning-2002]", "color_warning": "[Warning-2003]"}
COLOR_BOX = ["White", "Black", "Purple", "Yellow", "Orange", "Green", "Blue"]  # Color list for background and text
SIZE_BOX = ["50px", "100px", "200px", "360px", "500px"]  # list of size of images
IMFORMAT_BOX = ["jpg", "bmp", "png", "gif", "tiff", "JPG", "BMP", "PNG", "GIF",
                "TIFF"]  # list of supported image format
FONTSTYLE_BOX = ["normal", "italic", "oblique"]
FONT_FORMAT = [".ttf", ".woff", ".svg", ".eot"]
TARGET_BLANK = 'target="blank"'
CSS_MARGIN = '''margin-top: 50px;
    margin-bottom: 50px;
    margin-right: 50px;
    margin-left: 50px;
    border : 10px groove white;
    padding-top:10px;
    padding-bottom:20px;
    padding-left:10px;
    padding-right:10px;
    '''
CSS_ANIMATION_1 = '''
   animation-name: anim1;
    animation-duration: 4s;
    animation-fill-mode: both;
'''
CSS_ANIMATION_2 = '''
@keyframes anim1{
    0%{opacity: 0;}
    25%{opacity: 0.4;}
    50%{opacity:0.5;}
    75%{opacity:0.7;}
    100%{opacity: 1;}

}


'''
files = []
warnings = []
today_time = str(datetime.date.today())  # Get Today Date By datetime module


LOGO='''
  ____    ___
 / __ \  / _ \___ ____ ____
/ /_/ / / ___/ _ `/ _ `/ -_)
\___\_\/_/   \_,_/\_, /\__/
                 /___/
'''

LOREM_IPSUM='''
Lorem ipsum dolor sit amet, liber viris in ius, vel nihil malorum fuisset ut. Pro ullum discere ex, an sea suas purto menandri, libris verterem percipitur an pro. Cu ius sonet aperiri, iisque integre ancillae in pri, at labores verterem signiferumque pri. Ne est alienum cotidieque, graeci impetus consequat mei id. Ex vix malis vitae mucius, mel utinam invidunt ut.

Mel in sale vocent, eam diam quas ea. In probo putent duo, no putent persius delicatissimi est, nibh tation senserit ex has. Sed mundi imperdiet ut, pro at quidam alienum tibique. Qui decore offendit placerat no. No ceteros mnesarchum has.

Cibo viris ex nec. Te sed timeam apeirian. Aeterno quaestio at per, ex omnis commodo fuisset duo. His ea ipsum choro suscipiantur, ea eos voluptua definitiones, et per quodsi instructior.

Tale fabulas ei vel, mei natum etiam doctus ut, libris sanctus delectus sit at. Ex quot putant rationibus per, his ut eius erant nonumes, ei legere detraxit consequat mei. Ut vix habeo ubique consequuntur, quo eu omnis adversarium philosophia, ex paulo possim dolores sea. Pro porro graece latine ne. Vide timeam te sed, alia epicuri nostrum cu mea, putant intellegebat te mea. Case facer tractatos vim no, eu ius wisi imperdiet appellantur.

Vim an omnes fuisset salutandi, ea tollit insolens expetendis duo, te praesent mediocritatem qui. Est eu oratio option audire, ei mei elit insolens. Appellantur reformidans quo an, eum ne dicit veniam. Te vim alienum cotidieque, at meis tollit nominati eos.

Ne has illud ignota sensibus. Commodo erroribus vix ea, pri eros appareat id. Duo saepe putent omittam ei, dicit civibus pericula in vim. His id ludus suscipit comprehensam. Cum id pericula partiendo laboramus, iisque mandamus vituperata nec ut.

Id delectus eloquentiam pri, has falli zril mucius cu, vim id facilis appetere delicata. Sea ex tantas quodsi mentitum, ad omnis liber vim. Ad nam cetero petentium deseruisse, mel elit labitur labores in, qui tibique albucius vulputate ea. Cu vel commodo imperdiet abhorreant, unum appellantur no cum. In elitr cetero tamquam eum, aperiam explicari et nec.

Ne eripuit platonem ius. Nisl honestatis id sed, magna possim timeam vis ea, affert interesset ad per. Mel ut malorum delicata, elit habeo veritus eu per. Duo id nisl nostro, bonorum tibique rationibus mel an. Ex pro euismod erroribus, an reque deleniti sea.

Sapientem instructior ea vim. Sit congue expetenda persequeris in, soleat impedit ad duo, partiendo assueverit in nec. Nulla cetero conceptam ea mea, quo volumus appetere in. Suas omnium accusata te sea, id nec graeci assentior elaboraret.

Pro quis liberavisse ad, te sed mundi tibique accommodare. Vix paulo dictas suscipit an, cu tantas efficiendi mei. Affert reprehendunt te eam, et cibo mundi eos. Pro eu magna ludus consulatu, mea eu veritus reprimique. Pri et meis indoctum laboramus, magna impedit dolorem est eu.

Sea probo luptatum recteque ex. Unum alienum rationibus no cum, diceret equidem at vel, pro ex singulis salutandi. Sit natum ridens accusam eu, gloriatur voluptaria ex eam, convenire scripserit quaerendum vel ex. Sea ridens maiestatis in, no cum inermis suavitate, nobis assentior mel ad. Has omnis nulla at, no viris nominati his.

Quis congue latine ad eos. Integre suscipit sit id, te has eripuit comprehensam. At vix homero persecuti, ut qui dolor alterum legimus. Usu sint partem evertitur cu, no sea rebum labore. Liber facilis copiosae eos ei. Ius te accusam gubergren disputando, alii sale ius cu. Ea diam wisi salutandi eam, iriure partiendo posidonium ex per, eu exerci atomorum assueverit mea.

Iuvaret placerat ei vix, et aperiam sanctus mnesarchum has. Pri odio nihil nullam ad, ad impetus constituam sea, qui vivendum recteque ut. Causae scripserit concludaturque vel no, in vel sapientem voluptatum. Et atqui primis mel, id eos vitae signiferumque. Ne per nonumy eligendi, mei aliquip consulatu ne, qui ad feugiat impedit facilis. Ex sit dico blandit epicurei, illud iuvaret partiendo ut quo. Te cum delicata definiebas.

Vitae everti eam eu, utamur alterum legendos ne vim. Sit eu erant lobortis conceptam, vim id ubique minimum moderatius. Id nibh offendit disputando vim. Congue equidem singulis ad ius. Ius ut inani explicari.

Nec ea prompta laoreet intellegam, sit wisi atomorum ne. Ut alii tation nonumes eos. Eos enim solet imperdiet at, dolores neglegentur ius ne, his nobis forensibus te. Ut diam recusabo eum, vix ad adhuc docendi. Per solet gloriatur eloquentiam in.

Tota solum vix id, honestatis intellegebat ex nam. In duo natum reque fuisset, inani choro usu an, dicam veritus detraxit ut sea. Te ius copiosae gubergren, possim docendi eu pro. Cu iusto qualisque repudiandae sit, has ad tota urbanitas intellegebat, sea at decore persius intellegebat. Ne vim rebum euismod appetere. Ne sea elitr inimicus.

Qui ea nibh audiam nostrud. Eos no percipit maiestatis. Ex qui affert aliquando. Sed ad offendit tractatos, congue meliore perfecto pri in, ex elit soluta graeci sit. Quas fabellas reformidans vis cu, in mei partem diceret scriptorem.

Velit ponderum quaestio est ut. Legere imperdiet his te, semper interpretaris id eum. Iuvaret legimus facilisi mei et, labores veritus ea pri. Est veri liberavisse no, id aliquip adolescens pri. Quodsi labores ne usu.

Ius ignota corpora mediocritatem no, mel ne assum sonet albucius. Dicant voluptaria sed ut. Erant adipisci duo id, usu et aperiri voluptua scaevola, ut sea quis numquam. Viderer intellegebat no qui.

Ius aliquip tincidunt no, esse vide duis vix an. Cum habeo nonumes reprimique in. Ei eam cibo dicam habemus, est et eros everti, altera dolorem indoctum pri ad. Quo in nisl ludus invidunt, ei eam graecis necessitatibus, et eum assum oratio posidonium.

Eam in harum perfecto, vim accusata indoctum consequat ut. Ut corrumpit sententiae mei. Dico labores est in, vel epicuri forensibus ex. Id periculis accusamus sadipscing cum, ea quo corpora honestatis.

Id movet dicit eum. Putent everti aperiam duo ut, id nam ullum nominavi recusabo. Ea has assum indoctum, eu molestie evertitur consetetur eam, pri ad inimicus volutpat deseruisse. Vel no oporteat suscipiantur disputationi, sed justo numquam insolens eu, sed no justo oblique inermis. Malis deleniti lobortis et eum. Ius semper facilis constituam et, audire volutpat qui ea, odio nostro nostrud cu eum.

Doming facilisi mel eu. Tamquam aliquam indoctum mei te. Est paulo nominati intellegebat ex. Pro ne appetere inimicus, ut est tempor putant imperdiet. Eum in munere posidonium, nemore animal consetetur ne vix.

Ne usu veniam facete constituam, ut pro dico convenire adolescens. Vix eu summo elitr similique, vis vivendum philosophia ex. Vis in omnes dissentias, everti aliquam concludaturque duo no. Vim ea splendide gloriatur rationibus, case corpora vel in, ea mel natum commune intellegebat. No viderer diceret honestatis vel, ex tale instructior his.

Has volutpat dissentiunt ei, id vix viris invidunt. Est at odio rebum qualisque. Enim putent facilis cum no. Id mei dicam ubique. At mei euismod similique quaerendum, est minimum deserunt ea.

Ferri salutandi at nam, liber causae an has, laoreet evertitur similique vix ad. Ad per ferri novum sensibus. Idque causae argumentum mea et, nam animal nostrud posidonium te. Cu mel rebum lobortis torquatos. Pro id viris adipiscing, ne est vitae dicam. An vis enim eripuit expetendis, ad nam corpora percipit urbanitas. Cu pro duis tantas, eum virtute concludaturque at.

Novum dolorem te ius, ne cum accusata conclusionemque. Justo scaevola delicata mea ut, aperiam expetendis in pri. Id nec exerci eloquentiam dissentiunt, mel dictas incorrupte eu, ut dicant doming vis. Ferri commodo molestie nam ad.

Has summo mediocrem disputando in, mei mundi dolor probatus ne. An moderatius instructior mea, et diam mundi definitiones vix. Vim clita electram ut, habeo graeci vix cu. Vix ad quod odio theophrastus, sed nulla minimum disputationi eu. Vim te aperiam equidem dissentias, no inani legendos delicatissimi eum. Ex ubique perfecto adipisci est, ne qui velit indoctum.

Ei quo aeque cetero, per ut solum alterum, ei duo simul putent. Sed ad quas accusata, et suas tation invenire vis. Eum harum conclusionemque te, te vim singulis delicata. Ad pri vide minim maiorum. Ad rebum appareat assentior cum, saepe tation eu sit.

Cum tempor semper id, ius tota conceptam ad. Eos alterum verterem accusata et, quem torquatos no vix, at vix facer quando complectitur. Vim ea sale integre mediocrem, euismod assentior cum no. Altera vidisse ut usu, affert diceret qualisque nec ei. Eum eu amet minimum ullamcorper. Ad has errem omnes vivendum, mel homero labore ea, illum noster omittam at mea.

Sea ex accusam mentitum, vix inani falli ad, in quas viderer has. His postea adolescens reformidans ut, eu diam nusquam per, fierent deserunt pro ne. Ius eros magna probatus ei, scripta assueverit ut qui. Nam legere fabellas tincidunt an. Sit error omnium ex, cu omnis eirmod atomorum eam, eum partem noster iisque at.

Prima illud eloquentiam ea nam, eum eruditi detracto no, ne semper ocurreret reprimique vis. At aliquip ocurreret sea. Eum veri iudicabit ocurreret an, ei usu ornatus partiendo rationibus. Meis invidunt adolescens ei his. Vel saepe recteque consequuntur eu. Ea atomorum salutandi neglegentur eam, no mel reque consulatu, commune probatus consetetur has an. Sale causae ut duo, has tincidunt constituto argumentum ei, ei pro ipsum congue.

Ne decore invidunt mea, in inani soluta inermis nam. Pri legere facete eu, no facete voluptua platonem pro. Ut solum reque clita usu, cum ea saepe verterem argumentum. Ei duo tritani ornatus reprehendunt, ut suas veniam quaestio sit. Cu iuvaret perpetua pro.

Id mea prima aliquip mnesarchum, per quem oblique delicatissimi an. Id eam putent feugait, vis et mazim dicant molestie. Viderer vivendum nam cu, id suas suavitate his. Qui aperiam numquam labores cu, numquam voluptatibus nam an, cu integre ancillae sit. Recusabo consulatu eu eum, mel ipsum homero nostro id, in nihil aperiam sit.

Summo minimum te has, no vim partem discere persecuti. Alia oportere instructior est eu, at mei adolescens expetendis contentiones. Qui laudem admodum ex. In decore noluisse duo, mel te erat minim facete.

Ad tale dolore virtute pri, adhuc contentiones eu sea. Eum ea verear hendrerit, his an probo minim audire. Quo cu velit delectus, sit putant euismod in. Id mei facilis pericula, est eu falli detracto voluptaria, ex persius assentior pro. Laudem dignissim id eam.

Id homero dolorum sed, latine fierent ea est. Usu melius assueverit reprehendunt et, et iusto graece luptatum sed, porro viderer oporteat vix id. Duo te quidam viderer ullamcorper, est volutpat democritum te. Usu te apeirian erroribus. Usu ex nemore dictas utamur, diceret equidem mel ne. Ex vocibus nominati mei, enim aliquid referrentur pri ad.

Mei no sale nostro, an eam periculis conceptam. Ius choro decore ornatus an, per in quis postea mediocritatem, ex sale perfecto torquatos his. Eam oportere consetetur signiferumque id, no paulo maiestatis eum, ne facer legendos eos. Purto saepe te vis, pro mundi accusamus voluptatibus ne. Cum cu facer nonumes.

Has id vidisse sapientem, quando munere mnesarchum per id. Ea ubique blandit nec, eius iusto an cum. Cum ne partem adipisci. Deterruisset conclusionemque ei pri. Ne ferri omittam per, rationibus necessitatibus et vel. Et nec habemus officiis.

Id expetenda dissentiet appellantur quo. Est no summo nulla. Ex pro etiam vitae populo, at mea omnium detraxit. Mea id vocibus vivendum signiferumque, indoctum democritum duo ad.

Viderer delenit nam ne, ne iudico alterum per, maiorum detracto definitiones pri ex. Ea dico albucius constituam sit. Eam reque clita salutatus ne, aliquip theophrastus reprehendunt eam at. Volutpat petentium disputando duo eu, nam dolores sadipscing dissentiunt te. Duo dicam lobortis no, vide fabellas vis cu.

Tota ullum at cum. Docendi adolescens in usu, tollit albucius mea et. Cu eos enim nominavi sensibus. Dico graeci ea mea, sea ut dicam luptatum definitionem. Cum no ullum alienum urbanitas.

Iusto omittam mandamus mea an, enim simul eirmod at pri. Usu vivendo suscipit ex, vis in scaevola vivendum, qui dico scripta ne. Duo ei pericula euripidis, ex fierent prodesset constituam his. Per an iuvaret delicata temporibus, no ipsum paulo quo.

Cu pro everti argumentum, ne eum laboramus suscipiantur mediocritatem. Dolor graece expetendis id mei, has te everti recteque, cum cu diam movet noluisse. Sed ei mutat malorum, mea veri nostrum referrentur ex. Ut wisi aliquam suscipit duo, id mei dolorum molestiae.

Id magna commodo his, eius choro graeci in nec. Maiestatis assueverit an eos, ea vix dicam vidisse tritani. Ex sea quot dolore phaedrum. Decore partem vix eu. Sonet albucius inciderint ad mel, commune elaboraret his ne. Ei affert efficiantur cum, ex vim alterum convenire.

Putent putant an has. Eligendi interpretaris ei pro. Quo cibo luptatum assentior ex. No sea duis omnium. Novum oblique vivendum vel ad, ea mentitum facilisi eloquentiam nam.

Blandit senserit aliquando eam ei, alia soluta nostro ut sit, per id clita animal viderer. Dicat primis est no, porro accusata atomorum ei vix. Eam eu dolores quaerendum. Dolor numquam mel et. Semper percipit cum cu, summo reprehendunt an vim. Vim ea nostrum molestiae, et eam dicit dictas quaestio.

Pro detracto ponderum eu. Per vide omnium ex, te scripserit dissentiunt nam. Id erant fierent has, duo odio contentiones consectetuer ne, nonumes petentium sadipscing ne duo. Et vis summo feugait referrentur, at unum delectus eum. Everti scripserit liberavisse ei sed, et modo illud senserit mei. Pri ne debitis explicari, his malorum assentior in.

No dolor verterem pro. Clita ridens minimum ex nec. Ad quo case justo. Vix no blandit expetendis vituperata. Luptatum sensibus eum et, an utinam doming omnesque quo, nonumy causae sit ne. Pro wisi mucius invenire ut, ad sit delenit pertinax omittantur.

Mea ex rebum quaeque, no reque nostro hendrerit vis, meis vidisse theophrastus eu est. Ei has iisque labores dolorum. Mundi intellegebat vix ut, at usu eius regione torquatos. Case quando has ei, mei in natum tamquam minimum, utinam delicata pro te. Pro mazim latine vivendo an.

Movet postea quidam vix cu, ei assum inimicus dignissim vis. Sit ut assum perpetua, dictas tractatos urbanitas at vix. In mei sint persius indoctum, mea ne utinam oporteat. Electram erroribus intellegat nam an, qui et nominavi verterem. Eam ea nonumes disputationi.

Tota complectitur has an, est aliquip explicari liberavisse et. Ad liberavisse disputationi has, populo albucius te vix. Cum velit melius meliore in, est eu illud novum graece, in augue blandit sea. Cu pro mundi invenire, cu omnis sententiae sed. Vim in elit malorum tacimates.

Melius tincidunt intellegebat cum te, assum consetetur cu mel. Debitis eligendi ad pro, sea ut atqui oratio. Unum error labore est ne, eu bonorum erroribus vix. Te vix scaevola electram urbanitas, qui accusata definiebas id.

His cu regione reprehendunt. Solum vocent voluptua ne duo. Usu veritus corrumpit vituperatoribus id, ponderum hendrerit duo eu, ut veniam aliquid honestatis eam. Vix an reque iuvaret delicata, novum discere ut ius. Ex per alii dolores recteque.

Ut iuvaret qualisque est. Mei dolore insolens et. Ei sed latine commodo deleniti. Vel ad tollit vivendo, natum accumsan per at. Vidisse omittam definiebas mel ex, eam nemore virtute cu, ridens animal salutatus usu ex.

Purto everti feugiat an duo, id nisl decore perfecto eos. Velit alterum habemus at has. Sed habeo erant corrumpit ex, ius no mollis scribentur. Pro abhorreant necessitatibus no, sonet reformidans eu sit. Ut vix epicurei hendrerit, liber corrumpit ut ius.

His ei option regione tacimates, nostro convenire philosophia per ea. Ut eam nonumes mediocrem voluptatum, sit omnis simul graece ea, an quodsi nostrum sea. Cu per iusto reformidans, quo id vero timeam. Mea justo principes sententiae ex, ad sed rebum pertinax nominati. Vis virtute menandri reprimique te, ei sed noster prompta.

Possit oportere efficiendi qui ne, zril mucius democritum eu has. Sententiae efficiendi reformidans ne vix. Ei quem paulo timeam eos. Ut nam summo dicam. Quo ludus delenit ad. Quo cu novum insolens definitiones, nisl eligendi praesent ex vel.

Cum modus alienum quaestio et, at odio sumo vis. Admodum volumus splendide vix et. Ex sea percipitur disputando, complectitur mediocritatem nec eu. Quas posidonium efficiantur an sea, sit nibh reque aliquip ut. Cu mel ignota scribentur.

Et pri menandri necessitatibus, dicat noster his id, has te nisl justo admodum. Ad nonumes atomorum consetetur vim, mei mazim liber docendi ad. Qui omnesque patrioque in, an scriptorem intellegebat nec, vel errem nihil ad. Sed in tale impedit admodum, stet equidem dissentiunt mei ex. Vel mundi ludus ei, has ei illud referrentur disputationi, dicta patrioque duo an.

Nisl consetetur assueverit sed no, te sed lucilius insolens democritum. Ut facilis electram vel. Porro omnes ex pri, eu facer admodum est. Has ut accumsan nominavi percipit. Soleat consequat eum et, vix et dico gloriatur sadipscing, usu esse illum cu. Eros ridens eum ei.

Nonumes disputando ex per, falli feugiat pro te. At duo nihil audiam, malis legimus ancillae mei te. Zril accusam pericula per at. Eu qui fabellas corrumpit inciderint, te est simul cotidieque. Ne mea eirmod admodum, delenit suscipit inimicus ex vim.

Te possit prompta maluisset pro, est ea omnis nobis. Eum ei disputando vituperatoribus, in zril delicata definiebas eum. At vis eruditi apeirian, munere gloriatur vis id. Te qui cetero ponderum. Has et oratio causae definitionem, nemore adipiscing philosophia mel eu, ne vocibus maluisset aliquando quo. Salutandi philosophia ne ius. Ex illud augue utamur vis, ferri vocibus convenire vim an, pro persius docendi voluptaria te.

Pro id velit nemore propriae, quidam postulant ius ei. Nam at adipisci rationibus, eu qui esse corpora eleifend. Mel ornatus tacimates quaestio te, odio fabulas partiendo id ius. Tota munere at vim, primis doctus an vis. Ex perpetua conceptam qui. Saepe euripidis referrentur eu est, utroque expetendis an est.

His in solet aliquid. Cu vim quidam aliquando scribentur, per virtute adipisci et, ut errem legimus per. Vis albucius menandri instructior ad, eu quod tamquam appetere nec, est quaeque inermis accusamus te. Ex nec antiopam assentior, mei choro labitur adipiscing te. Ut quodsi urbanitas mei, pri accumsan mentitum neglegentur et, per sapientem principes ad. Eam an solum debitis, an dicta vitae vel. Sed id eros cotidieque ullamcorper, his ad nominavi hendrerit.

Quo sint tibique legendos et. Pri at cetero denique, ex decore doctus eam. Ex fabellas lucilius ius, ut cum case nihil feugiat. Case laoreet cu eos. Agam doming consectetuer ne eum, vix impetus insolens cu. Modus elaboraret contentiones in mel, qui omnium ornatus omittam cu, in alterum dignissim sit. Has te lorem dolorem nominati, ut stet congue has.

At pericula accommodare mea, vis perfecto consulatu mediocritatem ex, no quo ipsum nominavi. Fierent adipisci sit ad, sit quas dicunt ad. Habeo timeam fierent ad sit. Est no veniam volutpat, purto equidem te his, copiosae recteque id sit. Ea oporteat voluptaria definitiones vim, sea ad dolor regione, ei mea mutat equidem referrentur. Cu vim suscipit quaerendum, alterum ornatus vim ut.

Duo ne verterem lobortis vulputate, ei nusquam accusamus ius. At his accumsan sapientem, eam eu offendit sapientem. Duo ut facer oblique fabellas, nec dictas menandri scribentur ad. Amet theophrastus ad usu.

Eius alienum duo in, solum quaestio mel eu. Mei iriure ancillae eu, ne sed ignota urbanitas. Sit facete appetere cu. Cu eos primis vidisse dissentias.

Omnium scripserit scriptorem at est, graeco dolorum cu usu. Malis iudico maluisset et qui, mei debitis mediocrem an. Ea eos putant facilis delicata, ad pri laoreet reformidans adversarium, mea id pericula accusamus. Quo te iisque labores adolescens, te vidisse accusamus vulputate vis. Dicta maluisset reprimique te est. Ne sed postulant prodesset inciderint. Ceteros omittam reprimique nec eu, cum ex tota graeci adversarium, ne has quod eloquentiam.

Ne qui modo justo instructior, porro dolore doctus nam in, everti indoctum vel no. Ius appareat definitiones id, ad nec aeterno aliquid verterem. Nam ea detracto dissentias. Et eos dicunt graecis. Accusata salutatus mei no, an errem volumus voluptua sea.

Minimum accusam consetetur vis in, et quis nullam temporibus nam. An mea agam fuisset. Nullam facete omittam vis ex, oporteat mediocritatem has at. Veri virtute ea eos.

Te nulla habemus sea, at cum posse nullam voluptatibus, eros tamquam propriae sea et. Has maiorum gubergren et. Est at exerci ceteros. Cu nusquam mentitum oportere per, an noluisse tractatos mei. Pro at tempor dissentiet, ei vim wisi ferri deseruisse. Mei no audire dissentiet, est et rebum vivendo luptatum.

Has alia aliquam theophrastus in, cu eos posse summo. An quo cibo aeterno, eos novum solet mediocritatem an. Vel in rebum ludus, aeque inimicus partiendo usu eu. Est te harum tritani scriptorem, ex sumo euripidis est.

Ad sed rebum graece vivendo. Ex pri nostro regione philosophia. Mei eu meis feugait. Qui inani tamquam ceteros ex, ut eros ipsum vim. Vis ei audire feugiat fierent, vim in aperiam dolorem intellegam. Per ei suscipit delicata inimicus, duis urbanitas vulputate ne mel, corpora comprehensam id sit. Ius minim aeque sensibus ne, lorem dissentiet vim ne.

Pri partem scaevola oportere ut, usu invidunt pertinax pericula ad, tale atomorum instructior no eos. His et meliore invenire, nam eirmod suavitate an. Nam no saperet complectitur. Case laboramus ea mea, eu pri lorem postulant, ut quis postea dictas mel. Consul mediocritatem has ex, nulla laoreet intellegat nam an.

Vim tota zril nominati no. Ex est scripta aperiam maiorum. Mea ne animal cotidieque. Eos ex insolens phaedrum. Nec ad solum justo, eum porro rationibus an.

Mel nobis dolore convenire ex, scripta tacimates imperdiet his eu. Qui an tamquam menandri molestiae, wisi rationibus ne duo. Feugiat appareat interesset sea ei, ridens recteque qui ei, error omnium docendi ea duo. Per alterum postulant similique no, vel aperiri maiorum nusquam ea. Movet intellegebat ad pro, et vel facilisis iudicabit consectetuer, eum te fierent fabellas neglegentur. No per inimicus expetendis, eam purto suscipit apeirian ei, ut audiam quaestio ius.

Ne impetus deseruisse sea. Qui id nonumy vituperata scriptorem. Sed ad aliquid admodum omittantur. Iuvaret fuisset voluptua ne cum, sed menandri intellegebat an, aeterno feugiat facilisis pri cu. Sententiae eloquentiam pro ex. Per numquam singulis erroribus id, dolor homero eu vim.

Duo erant adolescens cu, at cum error zril doctus, insolens adipiscing duo an. Albucius deseruisse pri an, mea porro labitur placerat te, mea id solum error dissentiet. In eam quis omnis. Nec te debitis propriae ponderum. Qui agam instructior ex, quaeque nominavi pro ex. Nominati principes ex sit, ei scriptorem disputationi duo, an clita lobortis quo. Ad eos officiis sensibus forensibus, esse singulis disputationi ei nec, eum appareat scripserit te.

Saperet appellantur eos ad, stet alterum nam an. Sit ei accumsan voluptatibus. Ea his erant sapientem. Pri sint debitis civibus et. Cum an esse omittantur, eu nibh debitis qui, mel no suas ornatus senserit.

Mei prima illud neglegentur ad, novum deterruisset id vel. In ferri commodo philosophia eam, exerci corrumpit at nam. Cu eum summo vidisse. Velit habemus accommodare in has, ne tale eripuit urbanitas mel. No sit denique omittam mentitum. Ut vis sonet menandri iudicabit, vix sale discere deterruisset eu.

An idque harum has, nusquam consectetuer eos ea. Eam minimum blandit eu, audiam persecuti sadipscing sea ad, ut alii equidem ornatus vel. Ius ipsum aeque melius ea, justo honestatis at vis. Id unum oratio discere ius. Sed veniam causae iisque et, vim fugit dolores consetetur ea. Ridens reprehendunt et pri, in vix alia autem oratio, at per fugit detracto.

Sea in veri omnesque forensibus. Vix epicuri delectus referrentur te, ea erat prodesset contentiones sed. Quo ei vocent sapientem tincidunt, et graeci cetero scaevola vim. Ei iusto impedit cum, pro ancillae facilisis evertitur ne. Nec dolor essent reformidans te, id dicam nusquam per.

Et propriae suscipiantur sed. Te cum suas altera salutatus, no sonet legimus vim, ius audire albucius singulis no. Nec quem movet legimus ut. No eos vocibus concludaturque, vis ei amet voluptua scribentur. At pro aperiri omittam. An altera tincidunt nec, his ut labitur phaedrum, an eos melius comprehensam. Quo ne voluptua evertitur.

Platonem electram sea eu. Vix ancillae democritum ex, pri dolorum iudicabit erroribus ei. Probo aperiri eum ea, cibo forensibus mel an. Meliore vituperatoribus eos te. Ea mazim nobis libris per, pro at tantas legimus debitis. Sit ut lobortis disputationi, et dicit quaestio mel. Cu nibh saperet consectetuer vim, ei vel hinc tempor mucius.

Has ei zril mandamus recteque, vix denique petentium theophrastus at. Pro eu putent conceptam. In commodo singulis sit, mei scaevola deterruisset cu. Aeque instructior ut vix, congue expetenda duo ex, ne mel consul nusquam. Ne mazim imperdiet adolescens sed.

Minim blandit neglegentur vel eu. No diam persius quaerendum eum, at eam omnium ancillae, ad sea debitis adipiscing. Mel at congue comprehensam, cum ceteros mentitum insolens an. Vim id regione vivendo, ad vis minimum lucilius, vis mentitum persequeris ad. Sea no utroque postulant salutandi.

Suas facete vis in, verear suscipit quo id. Ferri iudicabit ei sed. Duo corrumpit rationibus cu, ei qui falli vivendo. Cu eos ipsum aliquando, diceret delenit platonem nam id.

Eligendi senserit ius no. Mentitum voluptatibus quo at, te eruditi omnesque sea. Vim discere cotidieque intellegebat ea, cum id laboramus hendrerit. Ea ius novum vocibus contentiones, copiosae comprehensam necessitatibus ne qui, aeque tibique indoctum id has. Dico similique disputando sed at, te ludus alterum cum.

Id aliquip offendit his, mundi maluisset ne duo, cu epicurei senserit sit. Vivendum deseruisse ex mel, quo habeo scripta voluptatibus ei. Debet zril ridens te pri. Ius minimum suavitate an, eos an dolore nonumes. Movet primis constituto et nec, nam menandri consequat ne.

Cu inani vocibus fuisset est, omnium vivendum ei mel, qui id invenire mediocritatem. Eam facilisis maiestatis at, nibh elitr admodum quo ne. Ei pri quas augue sanctus, vel dolores suavitate ex. Suscipit percipitur repudiandae an duo, sed hendrerit evertitur consectetuer eu. Malorum delenit propriae ei eam.

Ut vix virtute diceret. Ea maiorum constituto mei. Semper rationibus nam te, te agam quando usu. Vix ex summo aperiam reformidans, cum in dico nemore referrentur. Id ius nibh harum, mel facer reprimique ut, eum facete eligendi detraxit ne.

An meis omittantur liberavisse qui, minim oporteat efficiantur quo at. Cetero salutatus consetetur pri te, alii iudico latine ei est, vocibus liberavisse ut quo. Omnis illum assum nam in, ex pertinacia mediocritatem pro. Qui nostro causae verear ne, eos at dicit percipit. Dico commodo forensibus his id.

Semper oporteat repudiare an nam, cibo repudiandae ad has. Admodum prodesset voluptatibus vel id. Eam ea latine incorrupte, adhuc eirmod cu vim, mea an adhuc nulla nostro. Eu pro quod natum tibique, te epicuri ancillae philosophia cum, an vix molestie voluptaria delicatissimi. Vim urbanitas posidonium instructior te. Possim praesent vis no.

Brute consequat ei qui, audire regione euripidis cum ea. Probo iisque ullamcorper an eam, vim cu solet cetero iisque. In clita aperiri eruditi nec. Detracto placerat ius eu, ei eum prompta prodesset, omnium pertinax mnesarchum vel id.

In quo oportere reprimique, sumo liber animal te vim. Dictas corrumpit ei mel, vidisse moderatius sit an. Est ei aliquip feugait necessitatibus, alia delenit mea ut. At labores ancillae mei, sit no option nonumes oportere. No purto aperiam reformidans pri.

Fugit iracundia constituam mea et, no mea laudem vocibus epicurei. Nobis semper scriptorem vix no. Nonumy reprehendunt eam ad, an dico insolens scriptorem sea. Debet deleniti epicurei mei id. Id duo graeco fastidii sapientem.

Oratio utinam fastidii pro eu, at sea veri voluptatibus. Laudem definiebas eam id, dicit elitr mediocrem ei mel. Timeam omnesque in eos, nullam delectus honestatis ut sed. Munere virtute eligendi vim ex, iusto omnium equidem vix et, no dicit soluta denique quo. Tota persequeris sea an, at novum munere invidunt his, an sea platonem argumentum. Usu noluisse tractatos elaboraret eu. Cum simul graecis quaestio eu, habemus tacimates eam te.

Quando persius id sea, dicam audire fabulas duo et. Rebum ocurreret assentior eam an, enim soleat reprehendunt vim an. At aliquam graecis.
'''