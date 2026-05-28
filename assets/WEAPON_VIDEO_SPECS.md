# Spécifications des 3 vidéos d'armes

Ce document décrit ce que tu dois produire pour les 3 vidéos d'armes qui seront révélées par taps successifs derrière le dos de Nara.

## Format technique

| Paramètre | Valeur | Pourquoi |
|---|---|---|
| Container | **MP4** (H.264) | Compatibilité maximale sur mobile, iOS/Android. |
| Dimensions | **886 × 998 px** | Identiques au canvas de l'image Nara — alignement pixel-perfect, pas de redimensionnement. |
| Frame rate | **24-30 fps** | Suffisant, ne pas dépasser 30 pour limiter la taille. |
| Durée | **2-5 secondes** | Suffisant pour un cycle d'animation. Plus court = file plus petit. |
| Loop-friendly | **dernière frame ≈ première** | La vidéo joue en boucle, transition fluide nécessaire. |
| Audio | **aucun** (track audio retirée) | On gérera le son via une couche audio séparée plus tard. |
| Poids visé | **< 1 MB** par vidéo | Chargement mobile rapide. < 500 KB idéal. |

## Fond chroma key

**Couleur de fond : vert pur `#00FF00` (RGB 0, 255, 0).** Le shader chroma-key supprime cette couleur en temps réel et la rend transparente.

Règles strictes :
- **Aucun vert pur** dans l'arme elle-même (sinon des trous apparaîtront). Si ton arme contient du vert, utilise une autre couleur de fond (bleu pur `#0000FF` ou rose magenta `#FF00FF`) et préviens-moi pour que je change le `color` dans le HTML.
- **Fond uniforme**, pas de gradient ni de bruit (sinon des artéfacts type "fringe vert" persisteront).

Astuce : la plupart des outils ont un export "alpha → vert" automatique. Sinon, mets une couche de couleur unie en arrière-plan dans ton projet d'animation.

## Positionnement dans le frame

Le frame vidéo (886 × 998) est **aligné EXACTEMENT** sur l'image Nara, donc :
- Tu positionnes l'arme **là où elle doit apparaître** par rapport à Nara, dans la vidéo elle-même
- Centre canvas (443, 499) = centre du corps de Nara
- Côté droit du canvas (x>443) = côté gauche du personnage (la main qui tient le couteau, derrière son dos)

**Suggestion artistique :** l'arme "sort" depuis derrière son corps. Tu peux placer l'arme à environ :
- x = 540-700 (à droite de son corps)
- y = 580-720 (au niveau des hanches/main)

Mais tu peux faire comme tu veux. L'idée est qu'elle apparaît derrière elle.

## Outils de production possibles

- **After Effects** (référence pro) : timeline + export H.264, MP4
- **Premiere / Davinci Resolve** : import d'illustrations animées, export MP4
- **Procreate Dreams** (iPad) : animation 2D simple, export MP4
- **Blender** (gratuit) : si tu veux faire de la 3D ou de la 2D rigging
- **Canva / CapCut** : pour des animations simples (apparition, oscillation)

Pour un rendu Nara cohérent : style aquarelle légère, traits doux, palette désaturée (rouges sombres, brun, beige). Évite les couleurs flashy qui casseraient l'esthétique.

## Workflow final

1. Tu prépares 3 fichiers : `weapon_1.mp4`, `weapon_2.mp4`, `weapon_3.mp4`
2. Tu les mets dans `assets/` (ou un sous-dossier comme `assets/weapons/`)
3. Tu me dis "c'est prêt" et je remplace les 3 lignes `<video>` dans `nara.html` :

   ```html
   <video id="weapon-1-vid" src="assets/weapons/weapon_1.mp4" loop muted playsinline crossorigin="anonymous"></video>
   <video id="weapon-2-vid" src="assets/weapons/weapon_2.mp4" loop muted playsinline crossorigin="anonymous"></video>
   <video id="weapon-3-vid" src="assets/weapons/weapon_3.mp4" loop muted playsinline crossorigin="anonymous"></video>
   ```

   Et je change les 3 `color: #00FF00` partout (si tu as gardé le green standard).

## Idées de progression dramatique (à toi de voir)

Tu as 3 armes pour raconter une mini-histoire. Quelques pistes :

- **Escalade** : couteau de cuisine → machette → batte cloutée
- **Inattendu** : couteau → revolver → grenade (rupture absurde)
- **Symbolique** : couteau → vide (rien) → fleur (renoncement)
- **Méta** : couteau → smartphone → trophée (commentaire sur la violence)

Quel que soit ton choix, défends-le conceptuellement par rapport au "twist" Nara (révéler l'ambiguïté/dualité du personnage).
