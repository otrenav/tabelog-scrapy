
| [Website](http://links.otrenav.com/website) | [Twitter](http://links.otrenav.com/twitter) | [LinkedIn](http://links.otrenav.com/linkedin)  | [GitHub](http://links.otrenav.com/github) | [GitLab](http://links.otrenav.com/gitlab) | [CodeMentor](http://links.otrenav.com/codementor) |

---

# Tabelog Scrapy with Google Compute Engine (GCE)

- Omar Trejo
- February, 2017
- For Dr. Kensuke Teshima

This repository contains scraping code for a Tabelog (www.tabelog.com/en/)
using either a local environment or a Google Compute Engine (GCE) instance.
It's implemented using Python 2.7 and designed to work on Ubuntu 16.04. There
are 14 branches in total, where each branch contains a different subset of the
pages that need to be scrapped such that Tabelog's blocking mechanism is not
activated.

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

## Making the repository private

This repository is currently public so that we can clone it within the
GCE instance without having to make any configurations regardin SSH
keys. However, if we would like to keep the repository private, it can
be done and we would have to make an extra setup step for each GCE
instance. Since this is not desired to keep the code as easy to use
as possible, it's not currently implemented this way, and the repository
is kept public.

## Resources

- https://cloud.google.com/compute/docs/quickstart-linux
- https://cloud.google.com/resource-manager/docs/creating-managing-projects

## List of prefectures

The number of allowed requests before getting blocked seems to be around
70,000 requests. Try to group your servers to not require more than that
amount.

### Group 1

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Aichi | 47,758 |
| Akita | 6,350 |
| Aomori | 8,250 |

### Group 2

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Chiba | 30,764 |
| Ehime | 9,424 |
| Fukui | 6,184 |

### Group 3

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Fukuoka | 34,045 |
| Fukushima | 11,539 |
| Gifu | 14,145 |

### Group 4

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Gunma | 13,968 |
| Hiroshima | 17,812 |
| Hokkaido | 39,100 |

### Group 5

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Hyogo | 36,096 |
| Ibaraki | 15,317 |
| Ishikawa | 8,694 |
| Iwate | 7,567 |

### Group 6

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Kagawa | 7,147 |
| Kagoshima | 9,912 |
| Kanagawa | 46,685 |

### Group 7

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Kochi | 5,487 |
| Kumamoto | 10,160 |
| Kyoto | 21,112 |
| Mie | 11,257 |
| Miyagi | 14,176 |
| Miyazaki | 7,121 |

### Group 8

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Nagano | 17,366 |
| Nagasaki | 8,395 |
| Nara | 7,199 |
| Niigata | 13,762 |
| Oita | 7,931 |
| Okayama | 11,216 |
| Okinawa | 13,252 |

### Group 9

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Osaka | 66,526 |
| Saga | 4,929 |

### Group 10

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Saitama | 33,718 |
| Shiga | 6,732 |
| Shimane | 4,054 |
| Shizuoka | 25,124 |

### Group 11

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Tochigi | 13,360 |
| Tokushima | 5,254 |

### Groups 12 and 13

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Tokyo | 130,632 |

### Group 14

| Prefecture | Number of listed restaurants |
|------------|------------------------------|
| Tottori | 3,638 |
| Toyama | 6,550 |
| Wakayama | 7,130 |
| Yamagata | 7,642 |
| Yamaguchi | 8,180 |
| Yamanashi | 7,228 |

TODOs:

- Combine cleaning procedures into single process

---

> "The best ideas are common property."
>
> —Seneca
