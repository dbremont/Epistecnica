---
tags: [note, guia]
---

# A Guide to Long-Term Information Storage


> **On Digital Technologies (Copy Ad Infinitum):** With short-term and medium-term storage media, we can continuously create copies of data, ensuring its permanence.
> 

### **Guide to Long-Term Information Storage**

Long-term information storage requires durability, integrity, and accessibility over years or decades. This guide covers **storage media, redundancy, formats, and maintenance strategies**.

---

## **1. Choosing the Right Storage Medium**

Each medium has trade-offs in **longevity, cost, and accessibility**.

| Storage Medium | Estimated Lifespan | Pros | Cons |
| --- | --- | --- | --- |
| **Magnetic Hard Drives (HDDs)** | 5-10 years | Cheap, high capacity | Mechanical failure, data degradation |
| **Solid-State Drives (SSDs)** | 5-10 years | Fast, no moving parts | Bit rot, limited write cycles |
| **M-Disc (Blu-ray)** | 1000+ years (claimed) | Optical longevity | Lower capacity (50-100GB per disc) |
| **Tape (LTO-9, etc.)** | 30+ years | Very high capacity | Needs special drives, slow access |
| **Archival-Grade Paper** | 100+ years | No tech required | Bulky, not searchable digitally |
| **DNA Storage** (Experimental) | 1000+ years | Extreme density | High cost, future retrieval uncertain |

## **2. Redundancy and Backups**

Use the **3-2-1 Backup Rule**:

- **3 copies** of data
- **2 different storage media** (e.g., HDD + tape)
- **1 offsite copy** (cloud, remote storage)

### **RAID for Redundancy (Not a Backup)**

- **RAID 1 (Mirroring):** Good for redundancy
- **RAID 5/6:** Fault-tolerant, but risk of rebuild failure
- **RAID 10:** Best for speed & redundancy

## **3. Choosing Durable File Formats**

Long-term readability depends on **open, standard formats**:

- **Text:** Plain text (`.txt`), Markdown (`.md`), LaTeX (`.tex`)
- **Documents:** PDF/A (archival PDF), OpenDocument (`.odt`)
- **Images:** PNG, TIFF (no compression loss)
- **Audio:** FLAC (lossless)
- **Video:** FFV1, Matroska (`.mkv`)
- **Data:** CSV, JSON, XML (structured)
- **Code & Configs:** Git repositories (`.git` with backups)

Avoid proprietary formats (`.docx`, `.xlsx`) unless exported to open alternatives.

## **4. Data Integrity and Corruption Protection**

### **Error-Detecting Storage**

- **ZFS / Btrfs:** Checksums to detect corruption
- **PAR2 (Parity Files):** Redundant error correction
- **Archival Software:** `borgbackup`, `restic`, `tar` with `xz --check=crc32`

### **Regular Data Checks**

- **Checksum Validation:**
    
    ```bash
    sha256sum file.txt > file.txt.sha256
    sha256sum -c file.txt.sha256  # Verify later
    
    ```
    
- **Scrubbing Storage:**
    - ZFS: `zpool scrub pool_name`
    - Btrfs: `btrfs scrub start /mnt/disk`

## **5. Physical Storage Conditions**

- **HDDs & SSDs:** Store in **cool, dry places**, power on occasionally (~1/year).
- **Optical Discs:** Keep away from sunlight, extreme temperatures.
- **Tape Storage:** Store upright in **low humidity (40-50%)** and stable temperature.
- **Paper & Print Archives:** Acid-free paper, climate-controlled storage.

## **6. Migration & Future-Proofing**

- **Migrate Data Every 5-10 Years:** Prevents format obsolescence.
- **Keep Hardware & Software to Read Old Data:** (e.g., floppy drives, tape readers).
- **Document File Formats & Metadata:** Future users need instructions to interpret data.

## **7. Cloud and Offsite Storage**

| Provider | Features | Best For |
| --- | --- | --- |
| **AWS S3 Glacier** | Cold storage, high durability | Large-scale archival |
| **Backblaze B2** | Affordable, simple API | Personal backups |
| **Google Cloud Nearline** | Fast retrieval, enterprise-focused | Business continuity |
| **Internet Archive** | Free for public data | Open-access preservation |

Encrypt sensitive data before cloud storage:

```bash
gpg --symmetric --cipher-algo AES256 file.tar.gz

```

---

## References

- https://www.reddit.com/r/DataHoarder/comments/tqbdua/what_choices_are_there_for_longterm_data_storage/
- https://news.ycombinator.com/item?id=31149427
- https://news.ycombinator.com/item?id=34952950
- https://news.ycombinator.com/item?id=43391459
- [ ]  https://github.com/ArchiveBox/ArchiveBox?tab=readme-ov-file
