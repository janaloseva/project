# project

## *Projekta uzdevums:*

Projekta mērķis bija automatizēt ikdienas procesus, tāpēc bija nolēmts izveidot botu, kas automātiski atgādina lietotājam izpildīt noteiktus uzdevumus. Tas ir noderīgs, lai novērstu aizmirstību par svarīgiem darbiem konkrētā dienā un laikā.

`main.py` skripts ir uzdevumu pārvaldības programma, kas ļauj lietotājam izveidot jaunu atgadināumu, saņemt sarakstu ar uzdevumiem un apturēt programmu. 

## *Funkciju paskaidrojums:*

1. **Importētās bibliotēkas:**
   - `csv`: Izmantots CSV failu lasīšanai un rakstīšanai.
   - `os`: Lietots failu ceļu un pašreizējā kataloga pārvaldībai.
   - `datetime`: Lietots darbam ar datumu un laiku.
   - `multiprocessing.Process`: Izmantots fonā darbošanas procesa veidošanai un atgādinājumu pārbaudei.
   - `time.sleep`: Izmantots, lai aizkavētu fonā darbošanas procesa izpildi.

2. **Faila ceļš:**
   - `file_path` mainīgais norāda uz CSV faila ("tasks.csv") atrašanās vietu, kur tiek glabāti uzdevumu dati. To veido, izmantojot absolūto ceļu līdz pašreizējam katalogam.
 
3. **Funkcijas:**
   - `save_new_task(task_name: str, reminder_date: datetime)`: Nolasa esošos uzdevumus no CSV faila, pievieno jaunu uzdevumu un atjauno uzdevumu sarakstu failā.
   - `create_task()`: Ļauj lietotājam izveidot jaunu paziņojuma nosaukumu un atgādinājuma datumu. Tiek izsaukts `save_new_task`, lai pievienotu uzdevumu CSV failā.
   - `get_all_tasks()`: Nolasa visus uzdevumus no CSV faila un atgriež tos kā vārdnīcu.
   - `print_all_tasks()`: Izdrukā visus uzdevumus, sakārtotus pēc to izpildes termiņiem.
   - `check_if_should_remind()`: Darbojas fonā, pārbauda, vai kāds uzdevums ir nokavēts, un sūta e-pasta atgādinājumu. Atjauno CSV failu ar atlikušiem uzdevumiem.
   - `main()`: Galvenais programmas cikls, kur lietotājs var izvēlēties izveidot jaunu uzdevumu, iegūt visu uzdevumu sarakstu vai apturēt programmu.

4. **Izpilde:**
   - Skripts palaiž fonā darbojošo procesu (`reminder_process`), lai nepārtraukti pārbaudītu nokavētos uzdevumus un sūtītu atgādinājumus uz e-pastu.
   - Galvenais programmas cikls ļauj lietotājam mijiedarboties ar uzdevumu pārvaldības sistēmu.

5. **Izmantošana:**
   - Palaidot skriptu, tas prasīs izvelēties 1, 2 vai 3: "1 - izveidot jaunu uzdevumu", "2 - iegūt visu uzdevumu sarakstu" vai "3 - apturēt programmu".
   - Izvēloties "izveidot jaunu uzdevumu", būs jāuzraksta uzdevuma nosaukumu, atgādinājuma datumu un laiku norādītajā formātā.
   - Atgādinājumu process nepārtraukti pārbaudīs nokavētos uzdevumus un sūtīs e-pasta atgādinājumus.
   - Izvēloties "iegūt visu uzdevumu sarakstu", paradīsies saraksts ar iepriekšējiem uzdevumiem, kuri vēl netika sūtīti.
   - Izveloties "apturēt programmu", programma pabeigs sabu darbību.

`email_notification.py` fails satur funkciju, kas ļauj sūtīt e-pastu, un tās sastāv no vairākām svarīgām daļām:

1. **E-pasta iestatījumi:**
   - `sender_email`: E-pasta adrese, no kuras tiks nosūtīts ziņojums (pazinojumubots@gmail.com).
   - `receiver_email`: E-pasta adrese, uz kuru tiks nosūtīts ziņojums (ioanna.loseva@gmail.com).
   - `subject`: Temats, kas tiks izmantots e-pasta ziņojuma nosūtīšanā ("Notification").

2. **Ziņojuma veidošana:**
   - `msg`: `MIMEMultipart` objekts, kas ļauj izveidot ziņojumu ar vairākām daļām.
   - Uzstādīti svarīgākie ziņojuma lauki (no, kam un temats).

3. **SMTP servera iestatījumi:**
   - `smtp_server`: Adrese SMTP servera, kas tiks izmantots (smtp.gmail.com).
   - `smtp_port`: Porta numurs, kurā notiks savienojums ar SMTP serveri (587).
   - `smtp_username`: Lietotāja vārds, kas tiks izmantots SMTP servera autentifikācijai (pazinojumubots@gmail.com).
   - `smtp_password`: Parole, kas tiks izmantota SMTP servera autentifikācijai ("scdr bvpo hxrf feyv").

4. **Funkcija `send_email(msg_to_user: str)`:**
   - `send_email` funkcija ņem ziņojuma tekstu lietotāja ievadītajā (`msg_to_user`), pieliek to e-pasta ziņojuma daļai un sūta to uz norādītajām e-pasta adresēm.
   - `MIMEText` tiek pielikts teksta ziņojums ar norādīto veidu ('plain').
   - Pēc tam tiek mēģināts pieslēgties pide SMTP servera un nosūtīt ziņojumu.

5. **Izmēģināšana un kļūdu apstrāde:**
   - `try` un `except` bloki tiek izmantoti, lai apstrādātu iespējamās kļūdas (piemēram, problēmas ar savienojumu vai autentifikāciju).
   - Ja kļūda notiek, tā tiek iegūta un nekādā veidā netiek attēlota vai izvadīta.

Šī faila mērķis ir nodrošināt atsevišķu moduli e-pasta nosūtīšanai, kas var tikt izmantots galvenajā failā `main.py`.