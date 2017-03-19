# Tabelog Scrapy with Google Compute Engine (GCE)

This repository contains scraping code for a Tabelog (www.tabelog.com/en/)
using either a local environment or a Google Compute Engine (GCE) instance. 
It's implemented using Python 2.7 and designed to work on Ubuntu 16.04.

The idea is to not depend on various laptops locally to be able to scrape
results from Tabelog without getting blocked (due to the amount of requests). 
To achieve this, the approach is to run the code for each prefecture whose
data we want in a new GCE instance. Each new GCE instance gets a new and
different IP, so IP-blocks from Tabelog can be handled this way. Each GCE
is automatically turned off after it's scraping task is finished, to keep
the data even after the instance no longer exists, it is sent to a Google
Cloud Storage (GCS) bucket within the same Google Cloud project.

The code is also able to run locally. If only a few prefectures are needed
this may be the best approach. If for some reason the laptop's IP gets
blocked, you may fallback to the GCE approach.

- Omar Trejo
- March, 2017

## Instructions

1. Create GCE instance with defaults but change to:
   - Ubuntu 16.04 LTS with 10 GB
       - The code should work with any Linux OS. However,
         the `setup.sh` script is written for an Ubuntu
         16.04 LTS OS. If easyness of use is desired,
         make sure you select this OS.
   - Allow full access to all Cloud APIs
       - This is not strictly required, but it's easier
         than turning the specific APIs we need by hand
         and there's no security risk of doing so because
         this instances are turned on for brief periods
         of time.
   - Allow HTTP/HTTPS traffic
       - This is required to be able to do the scrapping.
   - NOTE: If you don't know how to do this, take a look
     at the resources provided below for GCE.
   - NOTE: Keep track of the `project`, `zone`, and `instance`
     names as we'll need them later to turn down the instance
     automatically.
2. Setup environment in the GCE instance's terminal:
   - Clone repository
       - `$ git clone https://github.com/otrenav/scrapy-tabelog`
   - Change directory to repository
       - `$ cd scrapy-tabelog`
   - Execute setup script
       - `$ bash setup.sh`
       - If this doesn't seem to work, you can execute each line
         manually in the terminal. This is just to make it easier.
3. Execute main function:
   - `$ python main.py ...` (see usage section)

## Usage

### Local environment

`$ python main.py --prefecture=<prefecture>`

The `prefecture` argument is optional. If it's not supplied all
prefectures will be scrapped automatically. The results will be
saved within the `scrapy/` diectory, and the name will depend
on the date and whether or not a specific prefecture was chosen.
If no prefecture was chosen, the string `all-prefectures` will
be prepended. If a prefecture was chosen, it's name in lowercase
will be prepended.

### Google Compute Engine

To be able to turn off the instance automatically after finishing
scraping, we need to specify the `project`, `zone`, and `instance`
names chosen when creating the instance. This will be sent to the
`main` file as such:

```
$ python main.py --prefecture=<prefecture>
                 --project=<google_cloud_project>
                 --zone=<google_cloud_zone>
                 --instance=<google_cloud_instance>
```

The `prefecture` argument is optional. If it's not supplied all
prefectures will be scrapped automatically. Save name conventions
as in the Local Environment case apply. However the data will be
saved to a GCS bucket. It will be stored under the same project
in Google Cloud.

The `project`, `zone`, and `instance` names are optional (even if
working inside a GCE). If we're in a GCE instance but these parameters
are not supplied, the code will execute as if it were inside a local
environment, and no GCE instance deletion will occur. If one of these
parameters is supplied, all must be supplied. If this is the case
the data will sill be saved within the same Google Cloud project, but
the instance will remain turned on until manually deleted. This may
increase billing and is not recommended.

> Warning: Google Cloud arguments are not checked to be valid
> within so you must be careful they are correct when using them.

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
