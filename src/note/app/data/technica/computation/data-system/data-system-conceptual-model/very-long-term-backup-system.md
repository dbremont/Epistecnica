# Very-Long Term Backup System


> Note: This is not really database related; is a hollistic approach to data backup and recovery.
> 

> **Data** — Actual content within the file. Does not include metadata such as file name or modification time.
> 

> **Metadata** — Data describing a file, such as file name, modification time, or permission.
> 

> **Chunks** — A part of a file. A big file is split into multiple chunks for easier handling.
> 

> **Packs** — Multiple chunks combined into one file for more efficient handling.
> 

> **Blobs** — File data (chunks or packs) stored in our backup medium.
> 

> **Snapshot** — One backup at a point in time is called a snapshot. Making an update to the backup creates a second snapshot.
> 

> **Backup Medium** — Where the backup is actually stored. It can be cloud storage or an external hard-drive.
> 

QA:

- Does the Physical Storage Medium Have to be always connected? If not how to automate verifications?
- Which format to use to store the data?

## Storage Medium

> Estimated Lifespan; Pros; Cons
> 
- **HDDs & SSDs:** Store in **cool, dry places**, power on occasionally (~1/year).
- **Optical Discs:** Keep away from sunlight, extreme temperatures.
- **Tape Storage:** Store upright in **low humidity (40-50%)** and stable temperature.

### Cloud

…

## **Error-Detecting Storage**

- **ZFS / Btrfs:** Checksums to detect corruption
- **PAR2 (Parity Files):** Redundant error correction
- **Archival Software:** `borgbackup`, `restic`, `tar` with `xz --check=crc32`

## Redundancy

> 

## File Formats

> 
- **Text:** Plain text (`.txt`), Markdown (`.md`), LaTeX (`.tex`)
- **Documents:** PDF/A (archival PDF), OpenDocument (`.odt`)
- **Images:** PNG, TIFF (no compression loss)
- **Audio:** FLAC (lossless)
- **Video:** FFV1, Matroska (`.mkv`)
- **Data:** CSV, JSON, XML (structured)
- **Code & Configs:** Git repositories (`.git` with backups)

## Storage Model

> 

## Security

> 

## Tools

- **BorgBackup**
- **Restic**
- PAR2
- **Rclone**
- Duplicati

## References

- [A Guide to Long-Term Information Storage](https://app.notion.com/p/A-Guide-to-Long-Term-Information-Storage-1afc0f5171ec8064b6a4d1b4ce09cee0?pvs=21)
- https://news.ycombinator.com/item?id=31149427
- https://news.ycombinator.com/item?id=34952950
- [Backup and recovery](https://archive.org/details/backuprecovery0000pres)
- https://www.usenix.org/conference/hotstorage17/program/presentation/kathpal
- https://dl.acm.org/doi/10.1145/1218063.1217957
- [A Guide to Cloud Storage](https://app.notion.com/p/A-Guide-to-Cloud-Storage-1afc0f5171ec802b871ff365bf64a588?pvs=21)
- [Storage System](note.html?n=technica/computation/operating-system/linux/conceptual-model-linux/storage-system.md)
- [https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/backup-recovery/backup-recovery.pdf](https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/backup-recovery/backup-recovery.pdf)
- [System](note.html?n=technica/computation/system.md)