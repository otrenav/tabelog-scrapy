# Tabelog Scrapy

This repository contains scraping code for a Tabelog (www.tabelog.com/en/)
using either a local environment or a Google Compute Engine. It's
implemented using Python 2.7 and designed to work on Ubuntu 16.04.

- Omar Trejo
- March, 2017

## Instructions

1. Create Google Compute instance with
   - Ubuntu 16.04 LTS with 10 GB
   - Allow HTTP/HTTPS traffic
   - All full access to all Cloud APIs
2. Setup environment
   - Clone repository
       - `$ git clone https://github.com/otrenav/scrapy-tabelog`
   - Change directory to repository
       - `$ cd scrapy-tabelog`
   - Execute setup script
       - `$ bash setup.sh`
3. Execute main function
   - `$ python main.py ...` (see usage section)

## Usage

## Local environment

`$ python main.py --prefecture=<prefecture>`

The `prefecture` argument is optional.

## Google Compute Engine

```
$ python main.py --prefecture=<prefecture>
                 --project=<google_cloud_project>
                 --zone=<google_cloud_zone>
                 --instance=<google_cloud_instance>
```

The `prefecture` argument is optional. The `project`, `zone`, and
`instance` arguments are optional, but if one is supplied all must
be supplied. These should be the parameters you use to create the
Google Compute Engine instance from step 1.

> Warniing: Google Cloud arguments are not checked to be valid within
> so you must be careful they are correct when using them.

## Resources

- https://cloud.google.com/compute/docs/quickstart-linux
- https://cloud.google.com/resource-manager/docs/creating-managing-projects

## List of prefectures

1. Aichi
2. Akita
3. Aomori
4. Chiba
5. Ehime
6. Fukui
7. Fukuoka
8. Fukushim
9. Gifu
10. Gunm
11. Hiroshima
12. Hokkaido
13. Hyogo
14. Ibaraki
15. Ishikawa
16. Iwate
17. Kagaw
18. Kagoshima
19. Kanagawa
20. Kochi
21. Kumamoto
22. Kyoto
23. Mie
24. Miyag
25. Miyazaki
26. Nagano
27. Nagasaki
28. Nara
29. Nigat
30. Oita
31. Okayama
32. Okinawa
33. Osaka
34. Saga
35. Saitama
36. Shig
37. Shimane
38. Shizuoka
39. Tochigi
40. Tokushima
41. Tokyo
42. Tottori
43. Toyam
44. Wakayama
45. Yamagata
46. Yamaguchi
47. Yamanashi
