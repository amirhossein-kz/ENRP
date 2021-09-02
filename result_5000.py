import numpy as np
import matplotlib.pyplot as plt
import math

# paramss =  {'grid_1': [915, 3363, 7347, 12867, 19923, 28515, 38643, 50307, 63507, 78243, 94515, 112323, 131667, 152547, 174963, 198915, 224403, 251427, 279987, 310083, 341715, 374883, 409587, 445827, 483603, 522915, 563763, 606147, 650067, 695523, 742515, 791043], 'grid_8': [2112, 5568, 10560, 17088, 25152, 34752, 45888, 58560, 72768, 88512, 105792, 124608, 144960, 166848, 190272, 215232, 241728, 269760, 299328, 330432, 363072, 397248, 432960, 470208, 508992, 549312, 591168, 634560, 679488, 725952, 773952, 823488], 'grid_32': [15360, 15360, 15360, 33792, 33792, 58368, 58368, 89088, 89088, 125952, 125952, 168960, 168960, 218112, 218112, 273408, 273408, 334848, 334848, 402432, 402432, 476160, 476160, 556032, 556032, 642048, 642048, 734208, 734208, 832512, 832512, 936960], 'grid_64': [61440, 61440, 61440, 61440, 61440, 61440, 61440, 135168, 135168, 135168, 135168, 233472, 233472, 233472, 233472, 356352, 356352, 356352, 356352, 503808, 503808, 503808, 503808, 675840, 675840, 675840, 675840, 872448, 872448, 872448, 872448, 1093632], 'grid_128': [245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 540672, 540672, 540672, 540672, 540672, 540672, 540672, 540672, 933888, 933888, 933888, 933888, 933888, 933888, 933888, 933888, 1425408], 'grid_2': [1068, 3660, 7788, 13452, 20652, 29388, 39660, 51468, 64812, 79692, 96108, 114060, 133548, 154572, 177132, 201228, 226860, 254028, 282732, 312972, 344748, 378060, 412908, 449292, 487212, 526668, 567660, 610188, 654252, 699852, 746988, 795660], 'grid_4': [1392, 4272, 8688, 14640, 22128, 31152, 41712, 53808, 67440, 82608, 99312, 117552, 137328, 158640, 181488, 205872, 231792, 259248, 288240, 318768, 350832, 384432, 419568, 456240, 494448, 534192, 575472, 618288, 662640, 708528, 755952, 804912], 'grid_16': [3840, 8448, 14592, 22272, 31488, 42240, 54528, 68352, 83712, 100608, 119040, 139008, 160512, 183552, 208128, 234240, 261888, 291072, 321792, 354048, 387840, 423168, 460032, 498432, 538368, 579840, 622848, 667392, 713472, 761088, 810240, 860928]}
# reportLoss =  {'grid_1': [0.018348414450883865, 0.009459867142140865, 0.005739852786064148, 0.003893427550792694, 0.002730943961068988, 0.0020569534972310066, 0.001512800226919353, 0.0012734080664813519, 0.0008787300903350115, 0.0007633966160938144, 0.0006017092964611948, 0.0005368131096474826, 0.0004366550128906965, 0.00038219819543883204, 0.00032287760404869914, 0.00027776940260082483, 0.00022445569629780948, 0.00019294710364192724, 0.0001776518765836954, 0.00018342507246416062, 0.0001503111852798611, 0.00017299292085226625, 0.00012481272278819233, 6.324650894384831e-05, 6.956227298360318e-05, 0.0002725880185607821, 0.00011308982357149944, 7.346570055233315e-05, 7.304888276848942e-05, 0.0073941489681601524, 6.750809552613646e-05, 9.077288268599659e-05], 'grid_8': [0.0445086769759655, 0.018891435116529465, 0.010492762550711632, 0.006246797740459442, 0.0035214393865317106, 0.0023571231868118048, 0.001754032215103507, 0.0012096477439627051, 0.0008714133291505277, 0.0006337130325846374, 0.0004991823225282133, 0.00035255783586762846, 0.00026193459052592516, 0.00019678423996083438, 0.00014556740643456578, 0.00011552296200534329, 8.403247920796275e-05, 6.45356994937174e-05, 5.250922549748793e-05, 4.179844836471602e-05, 3.5305896744830534e-05, 2.8690305043710396e-05, 2.378269527980592e-05, 2.0367824618006125e-05, 1.7982760255108587e-05, 1.500780308560934e-05, 1.387702923238976e-05, 1.2826698366552591e-05, 1.1085494406870566e-05, 9.347464583697729e-06, 8.342688488482963e-06, 8.460763638140634e-06], 'grid_32': [0.03474279120564461, 0.03299367427825928, 0.03336107358336449, 0.015791654586791992, 0.015322728082537651, 0.009493379853665829, 0.009237161837518215, 0.00550721725448966, 0.005442484747618437, 0.0028578471392393112, 0.002955511212348938, 0.0014195640105754137, 0.0014556047972291708, 0.0007517530466429889, 0.0007490715361200273, 0.00037165352841839194, 0.0003659479261841625, 0.0002167351049138233, 0.0002186077181249857, 0.00013827769726049155, 0.0001431517448509112, 8.148948836605996e-05, 7.96177118900232e-05, 4.860048647969961e-05, 5.0222173740621656e-05, 3.096841828664765e-05, 3.0729723221156746e-05, 2.0768453396158293e-05, 2.0133531506871805e-05, 1.3999770089867525e-05, 1.3860511899110861e-05, 9.796499398362357e-06], 'grid_64': [0.023825615644454956, 0.02313607558608055, 0.02287020906805992, 0.022641953080892563, 0.023203974589705467, 0.022639047354459763, 0.023576220497488976, 0.005221199244260788, 0.005191705655306578, 0.005252852104604244, 0.005155568476766348, 0.001606972306035459, 0.0015941092278808355, 0.0015570565592497587, 0.0016059058252722025, 0.000531841185875237, 0.0005246386863291264, 0.000539995264261961, 0.0005285530351102352, 0.0002256969892187044, 0.00022617912327405065, 0.00021829076285939664, 0.00022688605531584471, 0.00010870062396861613, 0.00010771492088679224, 0.00010717505210777745, 0.00011009626177838072, 5.643362965201959e-05, 5.620196316158399e-05, 5.446611612569541e-05, 5.45266957487911e-05, 2.960551319119986e-05], 'grid_128': [0.01667059399187565, 0.016747625544667244, 0.016618456691503525, 0.01662473939359188, 0.016833145171403885, 0.0168425552546978, 0.01680797152221203, 0.0164216086268425, 0.016806531697511673, 0.01678989641368389, 0.016699109226465225, 0.016703680157661438, 0.01647697389125824, 0.016490772366523743, 0.016933124512434006, 0.0014987069880589843, 0.0015151442494243383, 0.001482171006500721, 0.0015042612794786692, 0.0015194490551948547, 0.0015300300437957048, 0.0015040477737784386, 0.0015234719030559063, 0.0003681879607029259, 0.00038288591895252466, 0.0003765342407859862, 0.00038648894405923784, 0.00037848128704354167, 0.0003660728398244828, 0.00037589273415505886, 0.0003787516616284847, 0.00015029327187221497], 'grid_2': [0.02038220688700676, 0.00853357370942831, 0.005538934841752052, 0.003801779355853796, 0.002603734377771616, 0.0017382021760568023, 0.00130200176499784, 0.0009341013501398265, 0.0007122200331650674, 0.0005690676625818014, 0.0004079540667589754, 0.00035148378810845315, 0.00029224727768450975, 0.0002087673346977681, 0.00017373116861563176, 0.00014918314991518855, 0.0001087393902707845, 9.711795428302139e-05, 8.695945143699646e-05, 7.446403469657525e-05, 6.260422378545627e-05, 5.435053026303649e-05, 4.990567686036229e-05, 4.6934870624681935e-05, 4.483781958697364e-05, 4.025668022222817e-05, 3.5581382689997554e-05, 3.705021663336083e-05, 5.487541784532368e-05, 3.916036803275347e-05, 2.6364221412222832e-05, 2.3858141503296793e-05], 'grid_4': [0.03345764800906181, 0.015603925101459026, 0.007044108584523201, 0.004087328445166349, 0.0028647868894040585, 0.002015459118410945, 0.0014493092894554138, 0.0010374629637226462, 0.0008007626747712493, 0.0006218167836777866, 0.00045482534915208817, 0.00035779515746980906, 0.0002631585521157831, 0.00021318437939044088, 0.00015331379836425185, 0.00012177571625215933, 9.49255409068428e-05, 8.42648369143717e-05, 6.933727127034217e-05, 5.51573139091488e-05, 4.3749751057475805e-05, 3.7777826946694404e-05, 3.101896800217219e-05, 3.059089067392051e-05, 2.9200396966189146e-05, 2.3391430659103207e-05, 2.2306830942397937e-05, 1.8951663150801323e-05, 2.0596427930286154e-05, 1.7610445866012014e-05, 1.5248518138832878e-05, 1.4636377272836398e-05], 'grid_16': [0.042068999260663986, 0.0278499573469162, 0.019381936639547348, 0.011936882510781288, 0.008916310034692287, 0.005830386187881231, 0.003900053445249796, 0.0031539741903543472, 0.0019180667586624622, 0.0013974433531984687, 0.0009756171493791044, 0.0006682162056677043, 0.0004523392708506435, 0.00031538779148831964, 0.00023528360179625452, 0.0001609818427823484, 0.0001354384294245392, 9.459546708967537e-05, 7.357998401857913e-05, 5.71402779314667e-05, 4.600527972797863e-05, 3.650502912933007e-05, 3.0249364499468356e-05, 2.4091703380690888e-05, 1.9579358195187524e-05, 1.6270150808850303e-05, 1.3491971003531944e-05, 1.1713188541762065e-05, 1.0001559530792292e-05, 8.33472040540073e-06, 7.370282673946349e-06, 6.221332114364486e-06]}
# reportIter =  {'grid_1': [5000, 3357, 819, 507, 356, 343, 276, 255, 215, 187, 180, 182, 166, 147, 145, 136, 131, 113, 119, 112, 106, 97, 28, 28, 27, 152, 80, 74, 78, 75, 72, 66], 'grid_8': [5000, 5000, 5000, 2171, 1365, 1010, 874, 698, 585, 527, 451, 391, 362, 334, 297, 279, 254, 234, 216, 190, 185, 176, 163, 159, 147, 143, 132, 127, 120, 120, 109, 107], 'grid_32': [5000, 5000, 5000, 5000, 5000, 4608, 4415, 2699, 2667, 1932, 1903, 1509, 1517, 1266, 1269, 1051, 1079, 936, 946, 843, 834, 755, 763, 686, 687, 627, 623, 576, 580, 531, 536, 490], 'grid_64': [5000, 5000, 5000, 5000, 5000, 5000, 5000, 3776, 3789, 3779, 3777, 2529, 2510, 2514, 2526, 1887, 1887, 1899, 1886, 1515, 1513, 1513, 1522, 1269, 1272, 1271, 1263, 1084, 1079, 1087, 1078, 943], 'grid_128': [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 3270, 3279, 3278, 3275, 3282, 3278, 3277, 3287, 2315, 2308, 2304, 2323, 2296, 2301, 2310, 2314, 1777], 'grid_2': [5000, 2262, 816, 603, 435, 300, 262, 212, 181, 180, 152, 143, 133, 118, 105, 104, 90, 88, 84, 80, 80, 71, 68, 65, 64, 60, 56, 55, 54, 51, 49, 48], 'grid_4': [5000, 5000, 2036, 1107, 760, 624, 445, 379, 344, 307, 253, 227, 210, 201, 171, 166, 144, 146, 131, 122, 110, 114, 98, 92, 96, 89, 85, 81, 74, 73, 74, 70], 'grid_16': [5000, 5000, 5000, 5000, 3973, 2449, 1844, 1449, 1230, 1073, 919, 838, 765, 697, 631, 575, 542, 477, 462, 435, 418, 386, 362, 344, 330, 305, 294, 276, 265, 252, 245, 231]}
# minLoss =  {'grid_1': [0.01834237203001976, 0.009459400549530983, 0.005739852786064148, 0.0038853862788528204, 0.002730637788772583, 0.002045742003247142, 0.0015093734255060554, 0.0012233081506565213, 0.0008663504850119352, 0.0007632729830220342, 0.0006017092964611948, 0.0005283518694341183, 0.00042417505756020546, 0.0003636880428530276, 0.0003222014056518674, 0.0002678430755622685, 0.00021132148685865104, 0.00018622094648890197, 0.00017519379616715014, 0.00015099749725777656, 0.0001374453422613442, 0.0001538526121294126, 7.840892067179084e-05, 5.678613524651155e-05, 5.670222162734717e-05, 0.00024037272669374943, 7.839502359274775e-05, 7.195243961177766e-05, 7.304888276848942e-05, 6.685980770271271e-05, 4.9687791033647954e-05, 6.111873517511413e-05], 'grid_8': [0.0445086769759655, 0.018891435116529465, 0.010492762550711632, 0.006246797740459442, 0.0035214393865317106, 0.0023571231868118048, 0.001754032215103507, 0.0012096477439627051, 0.0008713194984011352, 0.0006337130325846374, 0.0004991823225282133, 0.00035250920336693525, 0.000261764187598601, 0.00019678423996083438, 0.00014556740643456578, 0.00011469790479168296, 8.396379416808486e-05, 6.421421130653471e-05, 5.150245124241337e-05, 4.1089409933192655e-05, 3.435559119679965e-05, 2.8338352421997115e-05, 2.329297967662569e-05, 2.0367824618006125e-05, 1.7435222616768442e-05, 1.4951899174775463e-05, 1.2954813428223133e-05, 1.1736816304619424e-05, 1.0524045137572102e-05, 9.138595487456769e-06, 8.093220458249561e-06, 7.723204362264369e-06], 'grid_32': [0.03474279120564461, 0.03299367427825928, 0.03336107358336449, 0.015791654586791992, 0.015322728082537651, 0.009493379853665829, 0.009237161837518215, 0.00550721725448966, 0.005442484747618437, 0.0028578471392393112, 0.002955511212348938, 0.0014195640105754137, 0.0014556047972291708, 0.0007517530466429889, 0.0007490715361200273, 0.00037165352841839194, 0.0003659479261841625, 0.0002167351049138233, 0.0002186077181249857, 0.00013827769726049155, 0.0001431517448509112, 8.148948836605996e-05, 7.96177118900232e-05, 4.860048647969961e-05, 5.0222173740621656e-05, 3.096841828664765e-05, 3.0729723221156746e-05, 2.0768453396158293e-05, 2.011093238252215e-05, 1.3999770089867525e-05, 1.3860511899110861e-05, 9.789418982109055e-06], 'grid_64': [0.023825615644454956, 0.02313607558608055, 0.02287020906805992, 0.022641953080892563, 0.023203974589705467, 0.022639047354459763, 0.023576220497488976, 0.005221199244260788, 0.005191705655306578, 0.005252852104604244, 0.005155568476766348, 0.001606972306035459, 0.0015941092278808355, 0.0015570565592497587, 0.0016059058252722025, 0.000531841185875237, 0.0005246386863291264, 0.000539995264261961, 0.0005285530351102352, 0.0002256969892187044, 0.00022617912327405065, 0.00021829076285939664, 0.00022688605531584471, 0.00010870062396861613, 0.00010771492088679224, 0.00010717505210777745, 0.00011009626177838072, 5.643362965201959e-05, 5.620196316158399e-05, 5.446611612569541e-05, 5.45266957487911e-05, 2.960551319119986e-05], 'grid_128': [0.01667059399187565, 0.016747625544667244, 0.016618456691503525, 0.01662473939359188, 0.016833145171403885, 0.0168425552546978, 0.01680797152221203, 0.0164216086268425, 0.016806531697511673, 0.01678989641368389, 0.016699109226465225, 0.016703680157661438, 0.01647697389125824, 0.016490772366523743, 0.016933124512434006, 0.0014987069880589843, 0.0015151442494243383, 0.001482171006500721, 0.0015042612794786692, 0.0015194490551948547, 0.0015300300437957048, 0.0015040477737784386, 0.0015234719030559063, 0.0003681879607029259, 0.00038288591895252466, 0.0003765342407859862, 0.00038648894405923784, 0.00037848128704354167, 0.0003660728398244828, 0.00037589273415505886, 0.0003787516616284847, 0.00015029327187221497], 'grid_2': [0.02038208767771721, 0.008530324324965477, 0.005538820289075375, 0.0038015819154679775, 0.002603734377771616, 0.0017342641949653625, 0.0012932902900502086, 0.000930070411413908, 0.0007032244466245174, 0.0005681565380655229, 0.00040409862413071096, 0.00035038177156820893, 0.0002803766983561218, 0.000201028014998883, 0.0001708479830995202, 0.00014615888358093798, 0.000104661172372289, 9.156277519650757e-05, 8.400037768296897e-05, 7.023129001026973e-05, 6.244749238248914e-05, 5.1312497816979885e-05, 4.5674838474951684e-05, 4.5050073822494596e-05, 4.2060797568410635e-05, 3.9766931877238676e-05, 3.0897044780431315e-05, 3.2984571589622647e-05, 2.8774167731171474e-05, 3.295563510619104e-05, 2.3281572794076055e-05, 2.003522968152538e-05], 'grid_4': [0.03345764800906181, 0.015603925101459026, 0.007044108584523201, 0.0040863677859306335, 0.0028647868894040585, 0.0020152884535491467, 0.001448160968720913, 0.0010374629637226462, 0.000799788162112236, 0.0006211547879502177, 0.00045449513709172606, 0.00035741267492994666, 0.0002630390226840973, 0.00020982488058507442, 0.00015112906112335622, 0.00012042680464219302, 9.390186460223049e-05, 7.798241858836263e-05, 6.135662988526747e-05, 5.4382522648666054e-05, 4.072822775924578e-05, 3.6415192880667746e-05, 3.094158455496654e-05, 2.72188972303411e-05, 2.554605816840194e-05, 2.169781510019675e-05, 1.9689439795911312e-05, 1.8132112018065527e-05, 1.6795798728708178e-05, 1.513960069132736e-05, 1.4535870832332876e-05, 1.3549902178056072e-05], 'grid_16': [0.042068999260663986, 0.0278499573469162, 0.019381936639547348, 0.011936882510781288, 0.008916310034692287, 0.005830386187881231, 0.003900053445249796, 0.0031539741903543472, 0.0019180667586624622, 0.0013974433531984687, 0.0009756171493791044, 0.0006682162056677043, 0.0004523392708506435, 0.00031538779148831964, 0.00023528360179625452, 0.0001609207974979654, 0.00013541910448111594, 9.459546708967537e-05, 7.350963278440759e-05, 5.706847514375113e-05, 4.597094812197611e-05, 3.6318335332907736e-05, 2.9895785701228306e-05, 2.3939035600051284e-05, 1.9579358195187524e-05, 1.605184661457315e-05, 1.3415787179837935e-05, 1.138327206717804e-05, 9.688032150734216e-06, 8.204294317692984e-06, 7.151186764531303e-06, 6.221332114364486e-06]}

paramss =  {'grid_1': [915, 3363, 7347, 12867, 19923, 28515, 38643, 50307, 63507, 78243, 94515, 112323, 131667, 152547, 174963, 198915, 224403, 251427, 279987, 310083, 341715, 374883, 409587, 445827, 483603, 522915, 563763, 606147, 650067, 695523, 742515, 791043], 'grid_8': [2112, 5568, 10560, 17088, 25152, 34752, 45888, 58560, 72768, 88512, 105792, 124608, 144960, 166848, 190272, 215232, 241728, 269760, 299328, 330432, 363072, 397248, 432960, 470208, 508992, 549312, 591168, 634560, 679488, 725952, 773952, 823488], 'grid_32': [15360, 15360, 15360, 33792, 33792, 58368, 58368, 89088, 89088, 125952, 125952, 168960, 168960, 218112, 218112, 273408, 273408, 334848, 334848, 402432, 402432, 476160, 476160, 556032, 556032, 642048, 642048, 734208, 734208, 832512, 832512, 936960], 'grid_64': [61440, 61440, 61440, 61440, 61440, 61440, 61440, 135168, 135168, 135168, 135168, 233472, 233472, 233472, 233472, 356352, 356352, 356352, 356352, 503808, 503808, 503808, 503808, 675840, 675840, 675840, 675840, 872448, 872448, 872448, 872448, 1093632], 'grid_128': [245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 245760, 540672, 540672, 540672, 540672, 540672, 540672, 540672, 540672, 933888, 933888, 933888, 933888, 933888, 933888, 933888, 933888, 1425408], 'grid_2': [1068, 3660, 7788, 13452, 20652, 29388, 39660, 51468, 64812, 79692, 96108, 114060, 133548, 154572, 177132, 201228, 226860, 254028, 282732, 312972, 344748, 378060, 412908, 449292, 487212, 526668, 567660, 610188, 654252, 699852, 746988, 795660], 'grid_4': [1392, 4272, 8688, 14640, 22128, 31152, 41712, 53808, 67440, 82608, 99312, 117552, 137328, 158640, 181488, 205872, 231792, 259248, 288240, 318768, 350832, 384432, 419568, 456240, 494448, 534192, 575472, 618288, 662640, 708528, 755952, 804912], 'grid_16': [3840, 8448, 14592, 22272, 31488, 42240, 54528, 68352, 83712, 100608, 119040, 139008, 160512, 183552, 208128, 234240, 261888, 291072, 321792, 354048, 387840, 423168, 460032, 498432, 538368, 579840, 622848, 667392, 713472, 761088, 810240, 860928]}
reportLoss =  {'grid_1': [0.018262607976794243, 0.00922374241054058, 0.005930670537054539, 0.003802641062065959, 0.002660365542396903, 0.0020532049238681793, 0.0014631971716880798, 0.0011929054744541645, 0.0008841498056426644, 0.0007935602916404605, 0.0006541148759424686, 0.0005565875908359885, 0.0004506456898525357, 0.0003848812193609774, 0.0003062999458052218, 0.00028704869328066707, 0.00022980534413363785, 0.0002475519140716642, 0.0001546191779198125, 0.00017146626487374306, 0.0001411500124959275, 0.00019351384253241122, 0.00014547802857123315, 0.00011997668480034918, 9.471762314205989e-05, 0.000104672355519142, 0.00010567926801741123, 9.102192416321486e-05, 8.334085578098893e-05, 0.00012139265891164541, 6.0939892136957496e-05, 7.79461333877407e-05], 'grid_8': [0.0445086769759655, 0.018891435116529465, 0.010492762550711632, 0.006246797740459442, 0.0035214393865317106, 0.0023571231868118048, 0.001754032215103507, 0.0012096477439627051, 0.0008714133291505277, 0.0006337130325846374, 0.0004991823225282133, 0.00035255783586762846, 0.00026193459052592516, 0.00019678423996083438, 0.00014556740643456578, 0.00011552296200534329, 8.403247920796275e-05, 6.45356994937174e-05, 5.250922549748793e-05, 4.179844836471602e-05, 3.5305896744830534e-05, 2.8690305043710396e-05, 2.378269527980592e-05, 2.0367824618006125e-05, 1.7982760255108587e-05, 1.500780308560934e-05, 1.387702923238976e-05, 1.2826698366552591e-05, 1.1085494406870566e-05, 9.347464583697729e-06, 8.342688488482963e-06, 8.460763638140634e-06], 'grid_32': [0.03474279120564461, 0.03299367427825928, 0.03336107358336449, 0.015791654586791992, 0.015322728082537651, 0.009493379853665829, 0.009237161837518215, 0.00550721725448966, 0.005442484747618437, 0.0028578471392393112, 0.002955511212348938, 0.0014195640105754137, 0.0014556047972291708, 0.0007517530466429889, 0.0007490715361200273, 0.00037165352841839194, 0.0003659479261841625, 0.0002167351049138233, 0.0002186077181249857, 0.00013827769726049155, 0.0001431517448509112, 8.148948836605996e-05, 7.96177118900232e-05, 4.860048647969961e-05, 5.0222173740621656e-05, 3.096841828664765e-05, 3.0729723221156746e-05, 2.0768453396158293e-05, 2.0133531506871805e-05, 1.3999770089867525e-05, 1.3860511899110861e-05, 9.796499398362357e-06], 'grid_64': [0.023825615644454956, 0.02313607558608055, 0.02287020906805992, 0.022641953080892563, 0.023203974589705467, 0.022639047354459763, 0.023576220497488976, 0.005221199244260788, 0.005191705655306578, 0.005252852104604244, 0.005155568476766348, 0.001606972306035459, 0.0015941092278808355, 0.0015570565592497587, 0.0016059058252722025, 0.000531841185875237, 0.0005246386863291264, 0.000539995264261961, 0.0005285530351102352, 0.0002256969892187044, 0.00022617912327405065, 0.00021829076285939664, 0.00022688605531584471, 0.00010870062396861613, 0.00010771492088679224, 0.00010717505210777745, 0.00011009626177838072, 5.643362965201959e-05, 5.620196316158399e-05, 5.446611612569541e-05, 5.45266957487911e-05, 2.960551319119986e-05], 'grid_128': [0.01667059399187565, 0.016747625544667244, 0.016618456691503525, 0.01662473939359188, 0.016833145171403885, 0.0168425552546978, 0.01680797152221203, 0.0164216086268425, 0.016806531697511673, 0.01678989641368389, 0.016699109226465225, 0.016703680157661438, 0.01647697389125824, 0.016490772366523743, 0.016933124512434006, 0.0014987069880589843, 0.0015151442494243383, 0.001482171006500721, 0.0015042612794786692, 0.0015194490551948547, 0.0015300300437957048, 0.0015040477737784386, 0.0015234719030559063, 0.0003681879607029259, 0.00038288591895252466, 0.0003765342407859862, 0.00038648894405923784, 0.00037848128704354167, 0.0003660728398244828, 0.00037589273415505886, 0.0003787516616284847, 0.00015029327187221497], 'grid_2': [0.02038220688700676, 0.00853357370942831, 0.005538934841752052, 0.003801779355853796, 0.002603734377771616, 0.0017382021760568023, 0.00130200176499784, 0.0009341013501398265, 0.0007122200331650674, 0.0005690676625818014, 0.0004079540667589754, 0.00035148378810845315, 0.00029224727768450975, 0.0002087673346977681, 0.00017373116861563176, 0.00014918314991518855, 0.0001087393902707845, 9.711795428302139e-05, 8.695945143699646e-05, 7.446403469657525e-05, 6.260422378545627e-05, 5.435053026303649e-05, 4.990567686036229e-05, 4.6934870624681935e-05, 4.483781958697364e-05, 4.025668022222817e-05, 3.5581382689997554e-05, 3.705021663336083e-05, 5.487541784532368e-05, 3.916036803275347e-05, 2.6364221412222832e-05, 2.3858141503296793e-05], 'grid_4': [0.03345764800906181, 0.015603925101459026, 0.007044108584523201, 0.004087328445166349, 0.0028647868894040585, 0.002015459118410945, 0.0014493092894554138, 0.0010374629637226462, 0.0008007626747712493, 0.0006218167836777866, 0.00045482534915208817, 0.00035779515746980906, 0.0002631585521157831, 0.00021318437939044088, 0.00015331379836425185, 0.00012177571625215933, 9.49255409068428e-05, 8.42648369143717e-05, 6.933727127034217e-05, 5.51573139091488e-05, 4.3749751057475805e-05, 3.7777826946694404e-05, 3.101896800217219e-05, 3.059089067392051e-05, 2.9200396966189146e-05, 2.3391430659103207e-05, 2.2306830942397937e-05, 1.8951663150801323e-05, 2.0596427930286154e-05, 1.7610445866012014e-05, 1.5248518138832878e-05, 1.4636377272836398e-05], 'grid_16': [0.042068999260663986, 0.0278499573469162, 0.019381936639547348, 0.011936882510781288, 0.008916310034692287, 0.005830386187881231, 0.003900053445249796, 0.0031539741903543472, 0.0019180667586624622, 0.0013974433531984687, 0.0009756171493791044, 0.0006682162056677043, 0.0004523392708506435, 0.00031538779148831964, 0.00023528360179625452, 0.0001609818427823484, 0.0001354384294245392, 9.459546708967537e-05, 7.357998401857913e-05, 5.71402779314667e-05, 4.600527972797863e-05, 3.650502912933007e-05, 3.0249364499468356e-05, 2.4091703380690888e-05, 1.9579358195187524e-05, 1.6270150808850303e-05, 1.3491971003531944e-05, 1.1713188541762065e-05, 1.0001559530792292e-05, 8.33472040540073e-06, 7.370282673946349e-06, 6.221332114364486e-06]}
reportIter =  {'grid_1': [5000, 2893, 787, 530, 373, 346, 266, 250, 210, 197, 174, 191, 151, 150, 150, 141, 127, 122, 117, 111, 103, 98, 99, 87, 87, 84, 86, 78, 72, 71, 67, 67], 'grid_8': [5000, 5000, 5000, 2171, 1365, 1010, 874, 698, 585, 527, 451, 391, 362, 334, 297, 279, 254, 234, 216, 190, 185, 176, 163, 159, 147, 143, 132, 127, 120, 120, 109, 107], 'grid_32': [5000, 5000, 5000, 5000, 5000, 4608, 4415, 2699, 2667, 1932, 1903, 1509, 1517, 1266, 1269, 1051, 1079, 936, 946, 843, 834, 755, 763, 686, 687, 627, 623, 576, 580, 531, 536, 490], 'grid_64': [5000, 5000, 5000, 5000, 5000, 5000, 5000, 3776, 3789, 3779, 3777, 2529, 2510, 2514, 2526, 1887, 1887, 1899, 1886, 1515, 1513, 1513, 1522, 1269, 1272, 1271, 1263, 1084, 1079, 1087, 1078, 943], 'grid_128': [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 3270, 3279, 3278, 3275, 3282, 3278, 3277, 3287, 2315, 2308, 2304, 2323, 2296, 2301, 2310, 2314, 1777], 'grid_2': [5000, 2262, 816, 603, 435, 300, 262, 212, 181, 180, 152, 143, 133, 118, 105, 104, 90, 88, 84, 80, 80, 71, 68, 65, 64, 60, 56, 55, 54, 51, 49, 48], 'grid_4': [5000, 5000, 2036, 1107, 760, 624, 445, 379, 344, 307, 253, 227, 210, 201, 171, 166, 144, 146, 131, 122, 110, 114, 98, 92, 96, 89, 85, 81, 74, 73, 74, 70], 'grid_16': [5000, 5000, 5000, 5000, 3973, 2449, 1844, 1449, 1230, 1073, 919, 838, 765, 697, 631, 575, 542, 477, 462, 435, 418, 386, 362, 344, 330, 305, 294, 276, 265, 252, 245, 231]}
minLoss =  {'grid_1': [0.018261946737766266, 0.00922374241054058, 0.005894809495657682, 0.003801729530096054, 0.002651542890816927, 0.0020493268966674805, 0.0014582587173208594, 0.0011904226848855615, 0.0008776734466664493, 0.0007677701651118696, 0.0006186685641296208, 0.0005356677575036883, 0.00040890835225582123, 0.00035653539816848934, 0.0002933997311629355, 0.0002648767549544573, 0.00022482301574200392, 0.00019412252004258335, 0.00015362922567874193, 0.00013914002920500934, 0.00013938109623268247, 0.00015617869212292135, 0.00012120775500079617, 0.00010767554340418428, 8.879794040694833e-05, 8.040975080803037e-05, 7.334059046115726e-05, 7.569638546556234e-05, 5.8995181461796165e-05, 8.005155541468412e-05, 5.007748768548481e-05, 5.1529517804738134e-05], 'grid_8': [0.0445086769759655, 0.018891435116529465, 0.010492762550711632, 0.006246797740459442, 0.0035214393865317106, 0.0023571231868118048, 0.001754032215103507, 0.0012096477439627051, 0.0008713194984011352, 0.0006337130325846374, 0.0004991823225282133, 0.00035250920336693525, 0.000261764187598601, 0.00019678423996083438, 0.00014556740643456578, 0.00011469790479168296, 8.396379416808486e-05, 6.421421130653471e-05, 5.150245124241337e-05, 4.1089409933192655e-05, 3.435559119679965e-05, 2.8338352421997115e-05, 2.329297967662569e-05, 2.0367824618006125e-05, 1.7435222616768442e-05, 1.4951899174775463e-05, 1.2954813428223133e-05, 1.1736816304619424e-05, 1.0524045137572102e-05, 9.138595487456769e-06, 8.093220458249561e-06, 7.723204362264369e-06], 'grid_32': [0.03474279120564461, 0.03299367427825928, 0.03336107358336449, 0.015791654586791992, 0.015322728082537651, 0.009493379853665829, 0.009237161837518215, 0.00550721725448966, 0.005442484747618437, 0.0028578471392393112, 0.002955511212348938, 0.0014195640105754137, 0.0014556047972291708, 0.0007517530466429889, 0.0007490715361200273, 0.00037165352841839194, 0.0003659479261841625, 0.0002167351049138233, 0.0002186077181249857, 0.00013827769726049155, 0.0001431517448509112, 8.148948836605996e-05, 7.96177118900232e-05, 4.860048647969961e-05, 5.0222173740621656e-05, 3.096841828664765e-05, 3.0729723221156746e-05, 2.0768453396158293e-05, 2.011093238252215e-05, 1.3999770089867525e-05, 1.3860511899110861e-05, 9.789418982109055e-06], 'grid_64': [0.023825615644454956, 0.02313607558608055, 0.02287020906805992, 0.022641953080892563, 0.023203974589705467, 0.022639047354459763, 0.023576220497488976, 0.005221199244260788, 0.005191705655306578, 0.005252852104604244, 0.005155568476766348, 0.001606972306035459, 0.0015941092278808355, 0.0015570565592497587, 0.0016059058252722025, 0.000531841185875237, 0.0005246386863291264, 0.000539995264261961, 0.0005285530351102352, 0.0002256969892187044, 0.00022617912327405065, 0.00021829076285939664, 0.00022688605531584471, 0.00010870062396861613, 0.00010771492088679224, 0.00010717505210777745, 0.00011009626177838072, 5.643362965201959e-05, 5.620196316158399e-05, 5.446611612569541e-05, 5.45266957487911e-05, 2.960551319119986e-05], 'grid_128': [0.01667059399187565, 0.016747625544667244, 0.016618456691503525, 0.01662473939359188, 0.016833145171403885, 0.0168425552546978, 0.01680797152221203, 0.0164216086268425, 0.016806531697511673, 0.01678989641368389, 0.016699109226465225, 0.016703680157661438, 0.01647697389125824, 0.016490772366523743, 0.016933124512434006, 0.0014987069880589843, 0.0015151442494243383, 0.001482171006500721, 0.0015042612794786692, 0.0015194490551948547, 0.0015300300437957048, 0.0015040477737784386, 0.0015234719030559063, 0.0003681879607029259, 0.00038288591895252466, 0.0003765342407859862, 0.00038648894405923784, 0.00037848128704354167, 0.0003660728398244828, 0.00037589273415505886, 0.0003787516616284847, 0.00015029327187221497], 'grid_2': [0.02038208767771721, 0.008530324324965477, 0.005538820289075375, 0.0038015819154679775, 0.002603734377771616, 0.0017342641949653625, 0.0012932902900502086, 0.000930070411413908, 0.0007032244466245174, 0.0005681565380655229, 0.00040409862413071096, 0.00035038177156820893, 0.0002803766983561218, 0.000201028014998883, 0.0001708479830995202, 0.00014615888358093798, 0.000104661172372289, 9.156277519650757e-05, 8.400037768296897e-05, 7.023129001026973e-05, 6.244749238248914e-05, 5.1312497816979885e-05, 4.5674838474951684e-05, 4.5050073822494596e-05, 4.2060797568410635e-05, 3.9766931877238676e-05, 3.0897044780431315e-05, 3.2984571589622647e-05, 2.8774167731171474e-05, 3.295563510619104e-05, 2.3281572794076055e-05, 2.003522968152538e-05], 'grid_4': [0.03345764800906181, 0.015603925101459026, 0.007044108584523201, 0.0040863677859306335, 0.0028647868894040585, 0.0020152884535491467, 0.001448160968720913, 0.0010374629637226462, 0.000799788162112236, 0.0006211547879502177, 0.00045449513709172606, 0.00035741267492994666, 0.0002630390226840973, 0.00020982488058507442, 0.00015112906112335622, 0.00012042680464219302, 9.390186460223049e-05, 7.798241858836263e-05, 6.135662988526747e-05, 5.4382522648666054e-05, 4.072822775924578e-05, 3.6415192880667746e-05, 3.094158455496654e-05, 2.72188972303411e-05, 2.554605816840194e-05, 2.169781510019675e-05, 1.9689439795911312e-05, 1.8132112018065527e-05, 1.6795798728708178e-05, 1.513960069132736e-05, 1.4535870832332876e-05, 1.3549902178056072e-05], 'grid_16': [0.042068999260663986, 0.0278499573469162, 0.019381936639547348, 0.011936882510781288, 0.008916310034692287, 0.005830386187881231, 0.003900053445249796, 0.0031539741903543472, 0.0019180667586624622, 0.0013974433531984687, 0.0009756171493791044, 0.0006682162056677043, 0.0004523392708506435, 0.00031538779148831964, 0.00023528360179625452, 0.0001609207974979654, 0.00013541910448111594, 9.459546708967537e-05, 7.350963278440759e-05, 5.706847514375113e-05, 4.597094812197611e-05, 3.6318335332907736e-05, 2.9895785701228306e-05, 2.3939035600051284e-05, 1.9579358195187524e-05, 1.605184661457315e-05, 1.3415787179837935e-05, 1.138327206717804e-05, 9.688032150734216e-06, 8.204294317692984e-06, 7.151186764531303e-06, 6.221332114364486e-06]}


PIXEL_MAX = 1.0
for i in ['grid_1', 'grid_2', 'grid_4', 'grid_8', 'grid_16', 'grid_32', 'grid_64',]:# 'grid_128']:
    # j = 0
    # while j<len(paramss[i]) and paramss[i][j] <= 8e5:
    #     j += 1
    # if i == 'grid_64':
    #     plt.plot(paramss[i][:-1], 20 * np.log10(PIXEL_MAX / np.sqrt(minLoss[i][:-1])), label=i)
    # else:
    #     plt.plot(paramss[i], 20 * np.log10(PIXEL_MAX / np.sqrt(minLoss[i])), label=i)

    # if i == 'grid_64':
    #     plt.plot(paramss[i][:-1], 20 * np.log10(PIXEL_MAX / np.sqrt(minLoss[i][:-1])), label=i)
    # else:
    #     plt.plot(paramss[i], 20 * np.log10(PIXEL_MAX / np.sqrt(minLoss[i])), label=i)

    if i == 'grid_64':
        plt.plot(paramss[i][:-1], reportIter[i][:-1], label=i)
    else:
        plt.plot(paramss[i], reportIter[i], label=i)
plt.xlabel('#Weights')
# plt.ylim(0, 2000)
# plt.ylabel('PSNR')
plt.ylabel('#Iters')
plt.legend()
plt.savefig('iter_5000.eps')