#!/usr/bin/env bash
# ============================================================
#  STELLA FUGAZ (Peli 1) — Descarga organizada de assets
#  Crea "~/Desktop/stella assets/" con subcarpetas y renombra
#  cada imagen por tag + escena. Ejecuta esto en TU Mac/PC
#  (el CDN está bloqueado en el entorno remoto de Claude).
#
#  Uso:   bash download_stella_assets.sh
# ============================================================
set -uo pipefail

DEST="${HOME}/Desktop/stella assets"
B="https://d8j0ntlcm91z4.cloudfront.net/user_2xiUPlmEHgvD2pPzmlBd2jKDHRL"

mkdir -p "$DEST"/{01_locaciones,02_sublocaciones,03_personajes,04_naves,05_props,06_keyframes_arranque,07_keyframes_actos2-4,08_video}

ok=0; fail=0
dl(){ # $1 = ruta destino relativa   $2 = nombre de archivo remoto
  if curl -fsSL "$B/$2" -o "$DEST/$1"; then echo "  ✓ $1"; ok=$((ok+1));
  else echo "  ✗ FALLO: $1"; fail=$((fail+1)); fi
}

echo "Descargando en: $DEST"
echo "── 01 LOCACIONES ──"
dl "01_locaciones/LOC01_erdia_dorada_ESC2.png"            hf_20260624_081742_51c330ad-9baf-41f3-b8a7-36579ee8c515.png
dl "01_locaciones/LOC02_tierra_muerta_ESC1-2-33.png"      hf_20260624_081747_6cc66ac9-c1bd-489c-98bd-c923c1e79d82.png
dl "01_locaciones/LOC03_erdia_podrida_ESC22-31.png"       hf_20260624_101439_50982707-fa94-4f4f-9703-c0d0a12b0fa0.png
dl "01_locaciones/LOC04_palacio_pasillo_ESC3.png"         hf_20260624_081744_414dba37-0ae3-4d93-a141-bb80e4efd196.png
dl "01_locaciones/LOC05_taller_naio_ESC4-5.png"           hf_20260624_081745_53c4e86f-6df2-4972-8afd-e447c2e9e56e.png
dl "01_locaciones/LOC06_sala_trono_ESC25-30.png"          hf_20260624_081752_7e004230-3bc3-46e7-8ea2-071370a51324.png
dl "01_locaciones/LOC07_nave_nodriza_ESC8.png"            hf_20260624_081753_54199012-9318-4605-971a-806e52717519.png
dl "01_locaciones/LOC08_conductos_hangar_ESC6.png"        hf_20260624_081753_a8854b53-af65-4a37-b814-09984e6dbfc9.png
dl "01_locaciones/LOC09_espacio_orbita_ESC7.png"          hf_20260624_082131_23984f0c-f78c-4042-9fa0-0a8d3861f5ba.png
dl "01_locaciones/LOC10_nodriza_puente_ESC9-14-20.png"    hf_20260624_082133_71882f51-50a8-405a-90f8-29d882b23f51.png
dl "01_locaciones/LOC11_nodriza_bodega_ESC12-16.png"      hf_20260624_082135_37588edb-5ddc-44ae-b23b-74f0a7c4505a.png
dl "01_locaciones/LOC12_planeta_arido_ESC10.png"          hf_20260624_082136_57ef2fdc-3ce3-4644-98f5-4a7570863769.png
dl "01_locaciones/LOC13_planeta_batalla_ESC11.png"        hf_20260624_082138_1162cdbd-9ca4-4d94-bc4a-f8c9bc342330.png
dl "01_locaciones/LOC14_planeta_bosque_ESC13.png"         hf_20260624_082140_6e710200-7408-4050-b704-ec6109a021e9.png
dl "01_locaciones/LOC15_refugio_ESC17.png"                hf_20260624_082142_7662cc56-f0f2-444b-b3ff-8ba6e8cc52ef.png
dl "01_locaciones/LOC16_palacio_podrido_ESC15-18.png"     hf_20260624_101440_839488ae-4fef-440d-a02f-95d3dfe5bcdd.png
dl "01_locaciones/LOC17_sala_entrenamiento_ESC19.png"     hf_20260624_102515_722ac588-83d0-4038-9784-362c28c6b2ff.png
dl "01_locaciones/LOC18_nave_pequena_cabina_ESC21.png"    hf_20260624_082403_fb4fb043-f754-4cef-bb36-0d8f4cf7cbed.png
dl "01_locaciones/LOC19_nave_pequena_medica_ESC32.png"    hf_20260624_082404_219a4978-36b9-4b6e-9baf-b84ea558cb97.png

echo "── 02 SUB-LOCACIONES ──"
dl "02_sublocaciones/SUB01_sala_de_la_fuente_ESC5.png"    hf_20260624_111340_032708e7-b8e5-4ee5-84fd-d7843a681083.png
dl "02_sublocaciones/SUB02_hangar_ESC6.png"               hf_20260624_111342_718c17ce-9724-4fba-a118-11d2ccd85944.png
dl "02_sublocaciones/SUB03_poblado_resistencia_ESC22-23.png" hf_20260624_111345_635f3ea3-5cf6-49c7-adb3-0bd626ffe544.png
dl "02_sublocaciones/SUB04_cielo_erdia_ESC31.png"         hf_20260624_111347_411e1410-1ef6-4f9c-8ec5-feb31f6f0b9a.png

echo "── 03 PERSONAJES ──"
dl "03_personajes/stella_14_nina.png"                     hf_20260624_091602_91f736eb-90f3-44fb-9240-00f90d5b937d.png
dl "03_personajes/stella_22_guerrera.png"                 hf_20260624_115859_6bdaa4b4-df1c-4021-8ec0-99f53b149336.png
dl "03_personajes/stella_adulta_pelo_tenido.png"          hf_20260624_095631_13741e20-4a49-4d79-8861-a7b2baa921e0.png
dl "03_personajes/selka_4_bebe.png"                       hf_20260624_090448_ed9c4bf8-9b73-4c7e-8162-ce41d32efc05.png
dl "03_personajes/selka_general.png"                      hf_20260624_095629_7bcc38fc-46e6-4f27-a206-758ba7de893f.png
dl "03_personajes/selka_manca.png"                        hf_20260624_120820_1cb9a112-1fb6-4da7-afd7-ab5a2c4a1308.png
dl "03_personajes/vera_madre.png"                         hf_20260624_094034_277e86db-97b3-4c5f-b764-8fce170daba1.png
dl "03_personajes/vera_mayor_lider.png"                   hf_20260624_115354_00a3634d-dd4a-4066-8cde-c2705715846c.png
dl "03_personajes/naio_cientifico.png"                    hf_20260624_094038_cb71672a-63c0-4920-a85d-c589b54fbc47.png
dl "03_personajes/naio_esclavo.png"                       hf_20260624_115352_306bd14d-f487-4280-8f63-d4779d948f17.png
dl "03_personajes/gix_ajolote.png"                        hf_20260624_095627_6df90230-21c2-4307-addc-0eac562ef1dc.png
dl "03_personajes/gix_apagado.png"                        hf_20260624_120533_16d87dd7-e517-4f4e-9b8d-bdd7b2eb4340.png
dl "03_personajes/theron_cazador.png"                     hf_20260624_100446_b8b2b3fa-eba7-42cd-99c9-bc8323297d87.png
dl "03_personajes/brog.png"                               hf_20260624_095635_67ddd9dc-b7f6-4caa-9ff8-2382d7eea4fb.png
dl "03_personajes/nima.png"                               hf_20260624_094258_d5e105d9-d6fd-4f9c-8184-3ece926bca83.png
dl "03_personajes/noah_humano.png"                        hf_20260624_095636_a48d6010-9e41-4fe2-ae83-3b3eab2dcee0.png
dl "03_personajes/marek_rey_infiltrado.png"               hf_20260624_095904_6108f350-8742-4a28-9d64-5a0239646ae9.png
dl "03_personajes/vosk_maton.png"                         hf_20260624_095905_48370937-3227-49b2-b5c0-e9b74431c901.png
dl "03_personajes/rey_humano.png"                         hf_20260624_120310_4f83c96a-cc33-43ae-a6a8-7b102fbdb025.png
dl "03_personajes/vorthan_real_parasito.png"              hf_20260624_100448_90f40f08-627c-42eb-aaa1-3598f59f716f.png
dl "03_personajes/fig_g44_robot.png"                      hf_20260624_120519_29680ad0-7ab2-4799-91f9-f654cfc2decf.png
dl "03_personajes/fig_guardia_vacia.png"                  hf_20260624_120520_a27cefff-b40c-45fb-9fb2-8aa79e6731f3.png
dl "03_personajes/fig_korin.png"                          hf_20260624_120522_a9783998-ee0b-410b-8482-475f315a74b2.png
dl "03_personajes/fig_lessa.png"                          hf_20260624_120526_e21e917e-2a39-465a-b906-11da69fb93d0.png
dl "03_personajes/fig_guerrera_misteriosa.png"            hf_20260624_120534_80a4182f-a425-4747-a858-2c81bf7c705b.png

echo "── 04 NAVES ──"
dl "04_naves/capsula_huida_ESC6-7.png"                    hf_20260624_113908_10be0768-1ecb-4a11-b3e5-e81ea7604daa.png
dl "04_naves/naves_rey_cazas_ESC7.png"                    hf_20260624_113909_703c4928-73ae-4895-9b13-c95da4b6bd73.png
dl "04_naves/nave_nodriza_ext.png"                        hf_20260624_113910_117e667d-b005-4e37-b82b-26335a230a94.png
dl "04_naves/nave_pequena_ESC21-31-32.png"                hf_20260624_113912_b41e6a89-157e-4acd-a88e-68299423de8f.png
dl "04_naves/nave_vorthan_ESC31.png"                      hf_20260624_113914_fe40fd47-24ba-4ea4-8a73-9bc14c9c0b35.png

echo "── 05 PROPS ──"
dl "05_props/orbe_fuente_madre.png"                       hf_20260624_103603_d808886d-3915-482a-9f93-fe94a3123ce2.png
dl "05_props/brazalete_stella.png"                        hf_20260624_102941_b65e3b42-495e-4309-9535-802747d59a53.png
dl "05_props/rio_luzagua.png"                             hf_20260624_103405_8271de35-584b-4d7f-b255-a7c68d35a1c5.png
dl "05_props/fuente_plaza.png"                            hf_20260624_102511_527b5ac8-faf8-48d7-abe2-39ab70334bbb.png
dl "05_props/sable_selka.png"                             hf_20260624_103606_800951ae-d0ef-40e8-912d-c0118e34a5eb.png
dl "05_props/foto_familia.png"                            hf_20260624_115903_ae6856f1-e2c6-4911-a59b-76db77866ae4.png
dl "05_props/tanque_soporte.png"                          hf_20260624_115400_29a81683-aa02-47ce-a5ff-c48eec75166e.png

echo "── 06 KEY FRAMES · ARRANQUE (clips 1-8) ──"
dl "06_keyframes_arranque/KF_CLIP01_el_brote.png"          hf_20260624_113241_953abe92-5e88-49ab-9ca9-d6e998c335dc.png
dl "06_keyframes_arranque/KF_CLIP02_revelacion_erdia.png"  hf_20260624_112903_e562f1d5-7a0e-43d5-8b53-cd8730fbc300.png
dl "06_keyframes_arranque/KF_CLIP03_costumbre_paz.png"     hf_20260624_112905_ccc180a7-ff2b-42dd-8b27-e9492705bf17.png
dl "06_keyframes_arranque/KF_CLIP04_fuente_ninos.png"      hf_20260624_112922_cd6331c9-2c9d-4425-b142-a4c8bce6f816.png
dl "06_keyframes_arranque/KF_CLIP05_stella_corre_gix.png"  hf_20260624_112924_dee73d0e-5c6b-4450-a19d-028b73fc6921.png
dl "06_keyframes_arranque/KF_CLIP06_casi_choca_vera.png"   hf_20260624_112924_d0a0e21b-2b56-414b-8586-1deb49c21456.png
dl "06_keyframes_arranque/KF_CLIP07_leccion_orbe.png"      hf_20260624_112925_e4c0c1e9-ae47-4032-bf09-9192795c5f64.png
dl "06_keyframes_arranque/KF_CLIP08_la_anomalia.png"       hf_20260624_112926_f2e3d05a-7bbd-458c-a475-4931a493ed14.png

echo "── 07 KEY FRAMES · ACTOS 2-4 ──"
dl "07_keyframes_actos2-4/ESC05_la_caida.png"             hf_20260624_113916_042ac41b-cee8-47b9-94d0-eaccb363a317.png
dl "07_keyframes_actos2-4/ESC06-07_estrella_fugaz.png"    hf_20260624_113919_fd1c0597-db9e-4228-ab36-397f9ce03f90.png
dl "07_keyframes_actos2-4/ESC08_celda_nodriza.png"        hf_20260624_113920_a94bba23-3c83-49b9-aa5a-e4408dcf4228.png
dl "07_keyframes_actos2-4/ESC09_puente_theron.png"        ESC09_PENDIENTE.png
dl "07_keyframes_actos2-4/ESC10_combate_arido.png"        hf_20260624_114217_b34271d3-1afc-4d2b-9ca4-a6cdfbc4f407.png
dl "07_keyframes_actos2-4/ESC11_campo_batalla.png"        hf_20260624_114218_4ee7910f-e5e1-4d67-a175-e4d6601c4ecd.png
dl "07_keyframes_actos2-4/ESC13_lluvia_cometas.png"       hf_20260624_114219_0199dcf6-4e46-4b6b-b8c4-dd83908f9a5d.png
dl "07_keyframes_actos2-4/ESC14_theron_foto.png"          hf_20260624_114221_515299b3-7057-43d2-8700-e9005af8ee32.png
dl "07_keyframes_actos2-4/ESC17_refugio_vera.png"         hf_20260624_114225_01727623-c96c-40c5-88f6-4a2d62f17663.png
dl "07_keyframes_actos2-4/ESC18_palacio_podrido_naio.png" hf_20260624_114227_248d7160-aae8-42ce-b2d1-10834bd870d9.png
dl "07_keyframes_actos2-4/ESC19_la_traicion.png"          hf_20260624_114228_5a908509-a9b9-4875-aaa3-319eace17630.png
dl "07_keyframes_actos2-4/ESC21_stella_se_tine.png"       hf_20260624_114600_46adf335-4024-4534-a0e4-1b0da26c7352.png
dl "07_keyframes_actos2-4/ESC24_la_guerra.png"            hf_20260624_114602_2342c511-3784-48f5-9113-35106ffd0b47.png
dl "07_keyframes_actos2-4/ESC25-26_combate_trono.png"     hf_20260624_114605_4be136c7-78ba-4727-bff7-00d8dd16d504.png
dl "07_keyframes_actos2-4/ESC27_la_entrega.png"           hf_20260624_114606_b02e4653-3ff9-4c8f-93d9-b1a07b292aea.png
dl "07_keyframes_actos2-4/ESC28_metamorfosis_vorthan.png" hf_20260624_114610_3225c573-da11-48e0-9359-59f15122a3a8.png
dl "07_keyframes_actos2-4/ESC29_forma_real.png"           hf_20260624_114612_1a10e776-f080-4fad-b65e-4e7d740100ff.png
dl "07_keyframes_actos2-4/ESC31_cielo_despegue.png"       hf_20260624_114846_3b1906c4-f8d9-48e8-885b-c8b504824a7b.png
dl "07_keyframes_actos2-4/ESC32_bahia_medica.png"         hf_20260624_114848_2c363ee1-25fe-4e6d-803d-8e7d0f43032c.png

echo "── 08 VIDEO ──"
dl "08_video/CLIP01_el_brote_15s.mp4"                     hf_20260624_112443_8d74fc9b-743b-4eca-93c2-79eccea35d77.mp4

echo ""
echo "Listo. Descargadas: $ok · Fallos: $fail"
echo "Carpeta: $DEST"
[ "$fail" -gt 0 ] && echo "(Nota: ESC09 sale como PENDIENTE — actualiza su nombre de archivo cuando termine de generarse.)"
