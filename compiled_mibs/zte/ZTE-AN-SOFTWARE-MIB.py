# SNMP MIB module (ZTE-AN-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zte\ZTE-AN-SOFTWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:45 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zxAnSystem,) = mibBuilder.importSymbols(
    "ZTE-AN-SMI",
    "zxAnSystem")


# MODULE-IDENTITY

zxAnSoftwareMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30)
)
if mibBuilder.loadTexts:
    zxAnSoftwareMib.setRevisions(
        ("2011-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnSwObjects_ObjectIdentity = ObjectIdentity
zxAnSwObjects = _ZxAnSwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2)
)
_ZxAnCardSwObjects_ObjectIdentity = ObjectIdentity
zxAnCardSwObjects = _ZxAnCardSwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2)
)
_ZxAnSwCardRunningVerTable_Object = MibTable
zxAnSwCardRunningVerTable = _ZxAnSwCardRunningVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnSwCardRunningVerTable.setStatus("current")
_ZxAnSwCardRunningVerEntry_Object = MibTableRow
zxAnSwCardRunningVerEntry = _ZxAnSwCardRunningVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1)
)
zxAnSwCardRunningVerEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardSlot"),
)
if mibBuilder.loadTexts:
    zxAnSwCardRunningVerEntry.setStatus("current")
_ZxAnSwCardRack_Type = Integer32
_ZxAnSwCardRack_Object = MibTableColumn
zxAnSwCardRack = _ZxAnSwCardRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 1),
    _ZxAnSwCardRack_Type()
)
zxAnSwCardRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwCardRack.setStatus("current")
_ZxAnSwCardShelf_Type = Integer32
_ZxAnSwCardShelf_Object = MibTableColumn
zxAnSwCardShelf = _ZxAnSwCardShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 2),
    _ZxAnSwCardShelf_Type()
)
zxAnSwCardShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwCardShelf.setStatus("current")
_ZxAnSwCardSlot_Type = Integer32
_ZxAnSwCardSlot_Object = MibTableColumn
zxAnSwCardSlot = _ZxAnSwCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 3),
    _ZxAnSwCardSlot_Type()
)
zxAnSwCardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwCardSlot.setStatus("current")


class _ZxAnSwCardFileName_Type(DisplayString):
    """Custom type zxAnSwCardFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFileName_Object = MibTableColumn
zxAnSwCardFileName = _ZxAnSwCardFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 5),
    _ZxAnSwCardFileName_Type()
)
zxAnSwCardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileName.setStatus("current")


class _ZxAnSwCardFileType_Type(DisplayString):
    """Custom type zxAnSwCardFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFileType_Object = MibTableColumn
zxAnSwCardFileType = _ZxAnSwCardFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 6),
    _ZxAnSwCardFileType_Type()
)
zxAnSwCardFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileType.setStatus("current")


class _ZxAnSwCardVersion_Type(DisplayString):
    """Custom type zxAnSwCardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardVersion_Object = MibTableColumn
zxAnSwCardVersion = _ZxAnSwCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 7),
    _ZxAnSwCardVersion_Type()
)
zxAnSwCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardVersion.setStatus("current")
_ZxAnSwCardFileLen_Type = Integer32
_ZxAnSwCardFileLen_Object = MibTableColumn
zxAnSwCardFileLen = _ZxAnSwCardFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 8),
    _ZxAnSwCardFileLen_Type()
)
zxAnSwCardFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFileLen.setStatus("current")
_ZxAnSwCardBuildTime_Type = DateAndTime
_ZxAnSwCardBuildTime_Object = MibTableColumn
zxAnSwCardBuildTime = _ZxAnSwCardBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 9),
    _ZxAnSwCardBuildTime_Type()
)
zxAnSwCardBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBuildTime.setStatus("current")


class _ZxAnSwCardBootwareFileName_Type(DisplayString):
    """Custom type zxAnSwCardBootwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardBootwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareFileName_Object = MibTableColumn
zxAnSwCardBootwareFileName = _ZxAnSwCardBootwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 10),
    _ZxAnSwCardBootwareFileName_Type()
)
zxAnSwCardBootwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileName.setStatus("current")


class _ZxAnSwCardBootwareFileType_Type(DisplayString):
    """Custom type zxAnSwCardBootwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardBootwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareFileType_Object = MibTableColumn
zxAnSwCardBootwareFileType = _ZxAnSwCardBootwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 11),
    _ZxAnSwCardBootwareFileType_Type()
)
zxAnSwCardBootwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileType.setStatus("current")


class _ZxAnSwCardBootwareVersion_Type(DisplayString):
    """Custom type zxAnSwCardBootwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardBootwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardBootwareVersion_Object = MibTableColumn
zxAnSwCardBootwareVersion = _ZxAnSwCardBootwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 12),
    _ZxAnSwCardBootwareVersion_Type()
)
zxAnSwCardBootwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareVersion.setStatus("current")
_ZxAnSwCardBootwareFileLen_Type = Integer32
_ZxAnSwCardBootwareFileLen_Object = MibTableColumn
zxAnSwCardBootwareFileLen = _ZxAnSwCardBootwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 13),
    _ZxAnSwCardBootwareFileLen_Type()
)
zxAnSwCardBootwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareFileLen.setStatus("current")
_ZxAnSwCardBootwareBuildTime_Type = DateAndTime
_ZxAnSwCardBootwareBuildTime_Object = MibTableColumn
zxAnSwCardBootwareBuildTime = _ZxAnSwCardBootwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 14),
    _ZxAnSwCardBootwareBuildTime_Type()
)
zxAnSwCardBootwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardBootwareBuildTime.setStatus("current")


class _ZxAnSwCardFirmware1FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware1FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1FileName_Object = MibTableColumn
zxAnSwCardFirmware1FileName = _ZxAnSwCardFirmware1FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 15),
    _ZxAnSwCardFirmware1FileName_Type()
)
zxAnSwCardFirmware1FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileName.setStatus("current")


class _ZxAnSwCardFirmware1FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware1FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1FileType_Object = MibTableColumn
zxAnSwCardFirmware1FileType = _ZxAnSwCardFirmware1FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 16),
    _ZxAnSwCardFirmware1FileType_Type()
)
zxAnSwCardFirmware1FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileType.setStatus("current")


class _ZxAnSwCardFirmware1Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware1Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware1Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware1Version_Object = MibTableColumn
zxAnSwCardFirmware1Version = _ZxAnSwCardFirmware1Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 17),
    _ZxAnSwCardFirmware1Version_Type()
)
zxAnSwCardFirmware1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1Version.setStatus("current")
_ZxAnSwCardFirmware1FileLen_Type = Integer32
_ZxAnSwCardFirmware1FileLen_Object = MibTableColumn
zxAnSwCardFirmware1FileLen = _ZxAnSwCardFirmware1FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 18),
    _ZxAnSwCardFirmware1FileLen_Type()
)
zxAnSwCardFirmware1FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1FileLen.setStatus("current")
_ZxAnSwCardFirmware1BuildTime_Type = DateAndTime
_ZxAnSwCardFirmware1BuildTime_Object = MibTableColumn
zxAnSwCardFirmware1BuildTime = _ZxAnSwCardFirmware1BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 19),
    _ZxAnSwCardFirmware1BuildTime_Type()
)
zxAnSwCardFirmware1BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware1BuildTime.setStatus("current")


class _ZxAnSwCardFirmware2FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware2FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2FileName_Object = MibTableColumn
zxAnSwCardFirmware2FileName = _ZxAnSwCardFirmware2FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 20),
    _ZxAnSwCardFirmware2FileName_Type()
)
zxAnSwCardFirmware2FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileName.setStatus("current")


class _ZxAnSwCardFirmware2FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware2FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2FileType_Object = MibTableColumn
zxAnSwCardFirmware2FileType = _ZxAnSwCardFirmware2FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 21),
    _ZxAnSwCardFirmware2FileType_Type()
)
zxAnSwCardFirmware2FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileType.setStatus("current")


class _ZxAnSwCardFirmware2Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware2Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware2Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware2Version_Object = MibTableColumn
zxAnSwCardFirmware2Version = _ZxAnSwCardFirmware2Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 22),
    _ZxAnSwCardFirmware2Version_Type()
)
zxAnSwCardFirmware2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2Version.setStatus("current")
_ZxAnSwCardFirmware2FileLen_Type = Integer32
_ZxAnSwCardFirmware2FileLen_Object = MibTableColumn
zxAnSwCardFirmware2FileLen = _ZxAnSwCardFirmware2FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 23),
    _ZxAnSwCardFirmware2FileLen_Type()
)
zxAnSwCardFirmware2FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2FileLen.setStatus("current")
_ZxAnSwCardFirmware2BuildTime_Type = DateAndTime
_ZxAnSwCardFirmware2BuildTime_Object = MibTableColumn
zxAnSwCardFirmware2BuildTime = _ZxAnSwCardFirmware2BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 24),
    _ZxAnSwCardFirmware2BuildTime_Type()
)
zxAnSwCardFirmware2BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware2BuildTime.setStatus("current")


class _ZxAnSwCardFirmware3FileName_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3FileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware3FileName_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3FileName_Object = MibTableColumn
zxAnSwCardFirmware3FileName = _ZxAnSwCardFirmware3FileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 25),
    _ZxAnSwCardFirmware3FileName_Type()
)
zxAnSwCardFirmware3FileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileName.setStatus("current")


class _ZxAnSwCardFirmware3FileType_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3FileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware3FileType_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3FileType_Object = MibTableColumn
zxAnSwCardFirmware3FileType = _ZxAnSwCardFirmware3FileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 26),
    _ZxAnSwCardFirmware3FileType_Type()
)
zxAnSwCardFirmware3FileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileType.setStatus("current")


class _ZxAnSwCardFirmware3Version_Type(DisplayString):
    """Custom type zxAnSwCardFirmware3Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardFirmware3Version_Type.__name__ = "DisplayString"
_ZxAnSwCardFirmware3Version_Object = MibTableColumn
zxAnSwCardFirmware3Version = _ZxAnSwCardFirmware3Version_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 27),
    _ZxAnSwCardFirmware3Version_Type()
)
zxAnSwCardFirmware3Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3Version.setStatus("current")
_ZxAnSwCardFirmware3FileLen_Type = Integer32
_ZxAnSwCardFirmware3FileLen_Object = MibTableColumn
zxAnSwCardFirmware3FileLen = _ZxAnSwCardFirmware3FileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 28),
    _ZxAnSwCardFirmware3FileLen_Type()
)
zxAnSwCardFirmware3FileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3FileLen.setStatus("current")
_ZxAnSwCardFirmware3BuildTime_Type = DateAndTime
_ZxAnSwCardFirmware3BuildTime_Object = MibTableColumn
zxAnSwCardFirmware3BuildTime = _ZxAnSwCardFirmware3BuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 2, 1, 29),
    _ZxAnSwCardFirmware3BuildTime_Type()
)
zxAnSwCardFirmware3BuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardFirmware3BuildTime.setStatus("current")
_ZxAnSwSubcardRunningVerTable_Object = MibTable
zxAnSwSubcardRunningVerTable = _ZxAnSwSubcardRunningVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnSwSubcardRunningVerTable.setStatus("current")
_ZxAnSwSubcardRunningVerEntry_Object = MibTableRow
zxAnSwSubcardRunningVerEntry = _ZxAnSwSubcardRunningVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1)
)
zxAnSwSubcardRunningVerEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardSlot"),
)
if mibBuilder.loadTexts:
    zxAnSwSubcardRunningVerEntry.setStatus("current")
_ZxAnSwSubcardSlot_Type = Integer32
_ZxAnSwSubcardSlot_Object = MibTableColumn
zxAnSwSubcardSlot = _ZxAnSwSubcardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 1),
    _ZxAnSwSubcardSlot_Type()
)
zxAnSwSubcardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwSubcardSlot.setStatus("current")


class _ZxAnSwSubcardFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFileName_Object = MibTableColumn
zxAnSwSubcardFileName = _ZxAnSwSubcardFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 3),
    _ZxAnSwSubcardFileName_Type()
)
zxAnSwSubcardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileName.setStatus("current")


class _ZxAnSwSubcardFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFileType_Object = MibTableColumn
zxAnSwSubcardFileType = _ZxAnSwSubcardFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 4),
    _ZxAnSwSubcardFileType_Type()
)
zxAnSwSubcardFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileType.setStatus("current")


class _ZxAnSwSubcardVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardVersion_Object = MibTableColumn
zxAnSwSubcardVersion = _ZxAnSwSubcardVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 5),
    _ZxAnSwSubcardVersion_Type()
)
zxAnSwSubcardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardVersion.setStatus("current")
_ZxAnSwSubcardFileLen_Type = Integer32
_ZxAnSwSubcardFileLen_Object = MibTableColumn
zxAnSwSubcardFileLen = _ZxAnSwSubcardFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 6),
    _ZxAnSwSubcardFileLen_Type()
)
zxAnSwSubcardFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFileLen.setStatus("current")
_ZxAnSwSubcardBuildTime_Type = DateAndTime
_ZxAnSwSubcardBuildTime_Object = MibTableColumn
zxAnSwSubcardBuildTime = _ZxAnSwSubcardBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 7),
    _ZxAnSwSubcardBuildTime_Type()
)
zxAnSwSubcardBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBuildTime.setStatus("current")


class _ZxAnSwSubcardBootwareFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardBootwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareFileName_Object = MibTableColumn
zxAnSwSubcardBootwareFileName = _ZxAnSwSubcardBootwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 8),
    _ZxAnSwSubcardBootwareFileName_Type()
)
zxAnSwSubcardBootwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileName.setStatus("current")


class _ZxAnSwSubcardBootwareFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardBootwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareFileType_Object = MibTableColumn
zxAnSwSubcardBootwareFileType = _ZxAnSwSubcardBootwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 9),
    _ZxAnSwSubcardBootwareFileType_Type()
)
zxAnSwSubcardBootwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileType.setStatus("current")


class _ZxAnSwSubcardBootwareVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardBootwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardBootwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardBootwareVersion_Object = MibTableColumn
zxAnSwSubcardBootwareVersion = _ZxAnSwSubcardBootwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 10),
    _ZxAnSwSubcardBootwareVersion_Type()
)
zxAnSwSubcardBootwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareVersion.setStatus("current")
_ZxAnSwSubcardBootwareFileLen_Type = Integer32
_ZxAnSwSubcardBootwareFileLen_Object = MibTableColumn
zxAnSwSubcardBootwareFileLen = _ZxAnSwSubcardBootwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 11),
    _ZxAnSwSubcardBootwareFileLen_Type()
)
zxAnSwSubcardBootwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareFileLen.setStatus("current")
_ZxAnSwSubcardBootwareBuildTime_Type = DateAndTime
_ZxAnSwSubcardBootwareBuildTime_Object = MibTableColumn
zxAnSwSubcardBootwareBuildTime = _ZxAnSwSubcardBootwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 12),
    _ZxAnSwSubcardBootwareBuildTime_Type()
)
zxAnSwSubcardBootwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardBootwareBuildTime.setStatus("current")


class _ZxAnSwSubcardFirmwareFileName_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardFirmwareFileName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareFileName_Object = MibTableColumn
zxAnSwSubcardFirmwareFileName = _ZxAnSwSubcardFirmwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 13),
    _ZxAnSwSubcardFirmwareFileName_Type()
)
zxAnSwSubcardFirmwareFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileName.setStatus("current")


class _ZxAnSwSubcardFirmwareFileType_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardFirmwareFileType_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareFileType_Object = MibTableColumn
zxAnSwSubcardFirmwareFileType = _ZxAnSwSubcardFirmwareFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 14),
    _ZxAnSwSubcardFirmwareFileType_Type()
)
zxAnSwSubcardFirmwareFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileType.setStatus("current")


class _ZxAnSwSubcardFirmwareVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardFirmwareVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardFirmwareVersion_Object = MibTableColumn
zxAnSwSubcardFirmwareVersion = _ZxAnSwSubcardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 15),
    _ZxAnSwSubcardFirmwareVersion_Type()
)
zxAnSwSubcardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareVersion.setStatus("current")
_ZxAnSwSubcardFirmwareFileLen_Type = Integer32
_ZxAnSwSubcardFirmwareFileLen_Object = MibTableColumn
zxAnSwSubcardFirmwareFileLen = _ZxAnSwSubcardFirmwareFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 16),
    _ZxAnSwSubcardFirmwareFileLen_Type()
)
zxAnSwSubcardFirmwareFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareFileLen.setStatus("current")
_ZxAnSwSubcardFirmwareBuildTime_Type = DateAndTime
_ZxAnSwSubcardFirmwareBuildTime_Object = MibTableColumn
zxAnSwSubcardFirmwareBuildTime = _ZxAnSwSubcardFirmwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 3, 1, 17),
    _ZxAnSwSubcardFirmwareBuildTime_Type()
)
zxAnSwSubcardFirmwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardFirmwareBuildTime.setStatus("current")
_ZxAnSwImageTable_Object = MibTable
zxAnSwImageTable = _ZxAnSwImageTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnSwImageTable.setStatus("current")
_ZxAnSwImageEntry_Object = MibTableRow
zxAnSwImageEntry = _ZxAnSwImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1)
)
zxAnSwImageEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwImageFileName"),
)
if mibBuilder.loadTexts:
    zxAnSwImageEntry.setStatus("current")


class _ZxAnSwImageFileName_Type(DisplayString):
    """Custom type zxAnSwImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwImageFileName_Type.__name__ = "DisplayString"
_ZxAnSwImageFileName_Object = MibTableColumn
zxAnSwImageFileName = _ZxAnSwImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 1),
    _ZxAnSwImageFileName_Type()
)
zxAnSwImageFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwImageFileName.setStatus("current")


class _ZxAnSwImageFileType_Type(DisplayString):
    """Custom type zxAnSwImageFileType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwImageFileType_Type.__name__ = "DisplayString"
_ZxAnSwImageFileType_Object = MibTableColumn
zxAnSwImageFileType = _ZxAnSwImageFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 2),
    _ZxAnSwImageFileType_Type()
)
zxAnSwImageFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageFileType.setStatus("current")


class _ZxAnSwImageVersion_Type(DisplayString):
    """Custom type zxAnSwImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwImageVersion_Type.__name__ = "DisplayString"
_ZxAnSwImageVersion_Object = MibTableColumn
zxAnSwImageVersion = _ZxAnSwImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 3),
    _ZxAnSwImageVersion_Type()
)
zxAnSwImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageVersion.setStatus("current")
_ZxAnSwImageFileLen_Type = Integer32
_ZxAnSwImageFileLen_Object = MibTableColumn
zxAnSwImageFileLen = _ZxAnSwImageFileLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 4),
    _ZxAnSwImageFileLen_Type()
)
zxAnSwImageFileLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageFileLen.setStatus("current")
_ZxAnSwImageBuildTime_Type = DateAndTime
_ZxAnSwImageBuildTime_Object = MibTableColumn
zxAnSwImageBuildTime = _ZxAnSwImageBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 5),
    _ZxAnSwImageBuildTime_Type()
)
zxAnSwImageBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageBuildTime.setStatus("current")


class _ZxAnSwImageActiveStatus_Type(Integer32):
    """Custom type zxAnSwImageActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("none", 3))
    )


_ZxAnSwImageActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwImageActiveStatus_Object = MibTableColumn
zxAnSwImageActiveStatus = _ZxAnSwImageActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 6),
    _ZxAnSwImageActiveStatus_Type()
)
zxAnSwImageActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageActiveStatus.setStatus("current")
_ZxAnSwImageDownloadTime_Type = DateAndTime
_ZxAnSwImageDownloadTime_Object = MibTableColumn
zxAnSwImageDownloadTime = _ZxAnSwImageDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 2, 4, 1, 7),
    _ZxAnSwImageDownloadTime_Type()
)
zxAnSwImageDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwImageDownloadTime.setStatus("current")
_ZxAnSwUpdateObjects_ObjectIdentity = ObjectIdentity
zxAnSwUpdateObjects = _ZxAnSwUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3)
)
_ZxAnSwManualUpdateObjects_ObjectIdentity = ObjectIdentity
zxAnSwManualUpdateObjects = _ZxAnSwManualUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2)
)
_ZxAnSwManualUpdateGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSwManualUpdateGlobalObjects = _ZxAnSwManualUpdateGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1)
)
_ZxAnSwManualUpdateRack_Type = Integer32
_ZxAnSwManualUpdateRack_Object = MibScalar
zxAnSwManualUpdateRack = _ZxAnSwManualUpdateRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1, 1),
    _ZxAnSwManualUpdateRack_Type()
)
zxAnSwManualUpdateRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateRack.setStatus("current")
_ZxAnSwManualUpdateShelf_Type = Integer32
_ZxAnSwManualUpdateShelf_Object = MibScalar
zxAnSwManualUpdateShelf = _ZxAnSwManualUpdateShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1, 2),
    _ZxAnSwManualUpdateShelf_Type()
)
zxAnSwManualUpdateShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateShelf.setStatus("current")


class _ZxAnSwManualUpdateSlotList_Type(DisplayString):
    """Custom type zxAnSwManualUpdateSlotList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwManualUpdateSlotList_Type.__name__ = "DisplayString"
_ZxAnSwManualUpdateSlotList_Object = MibScalar
zxAnSwManualUpdateSlotList = _ZxAnSwManualUpdateSlotList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1, 3),
    _ZxAnSwManualUpdateSlotList_Type()
)
zxAnSwManualUpdateSlotList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSlotList.setStatus("current")


class _ZxAnSwManualUpdateSwType_Type(Integer32):
    """Custom type zxAnSwManualUpdateSwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bootware", 1)
    )


_ZxAnSwManualUpdateSwType_Type.__name__ = "Integer32"
_ZxAnSwManualUpdateSwType_Object = MibScalar
zxAnSwManualUpdateSwType = _ZxAnSwManualUpdateSwType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1, 4),
    _ZxAnSwManualUpdateSwType_Type()
)
zxAnSwManualUpdateSwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSwType.setStatus("current")


class _ZxAnSwManualUpdateSubcardList_Type(DisplayString):
    """Custom type zxAnSwManualUpdateSubcardList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwManualUpdateSubcardList_Type.__name__ = "DisplayString"
_ZxAnSwManualUpdateSubcardList_Object = MibScalar
zxAnSwManualUpdateSubcardList = _ZxAnSwManualUpdateSubcardList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 1, 5),
    _ZxAnSwManualUpdateSubcardList_Type()
)
zxAnSwManualUpdateSubcardList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSubcardList.setStatus("current")
_ZxAnSwManualUpdateStatusTable_Object = MibTable
zxAnSwManualUpdateStatusTable = _ZxAnSwManualUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnSwManualUpdateStatusTable.setStatus("current")
_ZxAnSwManualUpdateStatusEntry_Object = MibTableRow
zxAnSwManualUpdateStatusEntry = _ZxAnSwManualUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 5, 1)
)
zxAnSwManualUpdateStatusEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateSoftwareType"),
)
if mibBuilder.loadTexts:
    zxAnSwManualUpdateStatusEntry.setStatus("current")


class _ZxAnSwManualUpdateSoftwareType_Type(Integer32):
    """Custom type zxAnSwManualUpdateSoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bootware", 1)
    )


_ZxAnSwManualUpdateSoftwareType_Type.__name__ = "Integer32"
_ZxAnSwManualUpdateSoftwareType_Object = MibTableColumn
zxAnSwManualUpdateSoftwareType = _ZxAnSwManualUpdateSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 5, 1, 1),
    _ZxAnSwManualUpdateSoftwareType_Type()
)
zxAnSwManualUpdateSoftwareType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateSoftwareType.setStatus("current")


class _ZxAnSwManualUpdateStatus_Type(Integer32):
    """Custom type zxAnSwManualUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("negotiating", 1),
          ("downloading", 2),
          ("failed", 3),
          ("success", 4),
          ("sameversion", 5))
    )


_ZxAnSwManualUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSwManualUpdateStatus_Object = MibTableColumn
zxAnSwManualUpdateStatus = _ZxAnSwManualUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 5, 1, 2),
    _ZxAnSwManualUpdateStatus_Type()
)
zxAnSwManualUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwManualUpdateStatus.setStatus("current")


class _ZxAnSwManualFailedReason_Type(Integer32):
    """Custom type zxAnSwManualFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noSupportCardHwVersion", 2),
          ("mismatchCardHwVersion", 3),
          ("mismatchCardConfData", 4),
          ("noSwInNe", 5),
          ("cardUpdateSwFailed", 6))
    )


_ZxAnSwManualFailedReason_Type.__name__ = "Integer32"
_ZxAnSwManualFailedReason_Object = MibTableColumn
zxAnSwManualFailedReason = _ZxAnSwManualFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 5, 1, 3),
    _ZxAnSwManualFailedReason_Type()
)
zxAnSwManualFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwManualFailedReason.setStatus("current")
_ZxAnSwSubcardMUpdateStatusTable_Object = MibTable
zxAnSwSubcardMUpdateStatusTable = _ZxAnSwSubcardMUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnSwSubcardMUpdateStatusTable.setStatus("current")
_ZxAnSwSubcardMUpdateStatusEntry_Object = MibTableRow
zxAnSwSubcardMUpdateStatusEntry = _ZxAnSwSubcardMUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 6, 1)
)
zxAnSwSubcardMUpdateStatusEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardMUpdateSoftwareType"),
)
if mibBuilder.loadTexts:
    zxAnSwSubcardMUpdateStatusEntry.setStatus("current")


class _ZxAnSwSubcardMUpdateSoftwareType_Type(Integer32):
    """Custom type zxAnSwSubcardMUpdateSoftwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bootware", 1)
    )


_ZxAnSwSubcardMUpdateSoftwareType_Type.__name__ = "Integer32"
_ZxAnSwSubcardMUpdateSoftwareType_Object = MibTableColumn
zxAnSwSubcardMUpdateSoftwareType = _ZxAnSwSubcardMUpdateSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 6, 1, 1),
    _ZxAnSwSubcardMUpdateSoftwareType_Type()
)
zxAnSwSubcardMUpdateSoftwareType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwSubcardMUpdateSoftwareType.setStatus("current")


class _ZxAnSwSubcardMUpdateStatus_Type(Integer32):
    """Custom type zxAnSwSubcardMUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("negotiating", 1),
          ("downloading", 2),
          ("failed", 3),
          ("success", 4),
          ("sameversion", 5))
    )


_ZxAnSwSubcardMUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSwSubcardMUpdateStatus_Object = MibTableColumn
zxAnSwSubcardMUpdateStatus = _ZxAnSwSubcardMUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 6, 1, 2),
    _ZxAnSwSubcardMUpdateStatus_Type()
)
zxAnSwSubcardMUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardMUpdateStatus.setStatus("current")


class _ZxAnSwSubcardMUpdateFailedReason_Type(Integer32):
    """Custom type zxAnSwSubcardMUpdateFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("noSupportCardHwVersion", 2),
          ("mismatchCardHwVersion", 3),
          ("mismatchCardConfData", 4),
          ("noSwInNe", 5),
          ("cardUpdateSwFailed", 6))
    )


_ZxAnSwSubcardMUpdateFailedReason_Type.__name__ = "Integer32"
_ZxAnSwSubcardMUpdateFailedReason_Object = MibTableColumn
zxAnSwSubcardMUpdateFailedReason = _ZxAnSwSubcardMUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 2, 6, 1, 3),
    _ZxAnSwSubcardMUpdateFailedReason_Type()
)
zxAnSwSubcardMUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardMUpdateFailedReason.setStatus("current")
_ZxAnSwAutoUpdateObjects_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateObjects = _ZxAnSwAutoUpdateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3)
)
_ZxAnSwAutoUpdateGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateGlobalObjects = _ZxAnSwAutoUpdateGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1)
)
_ZxAnSwAutoUpdateChkObjects_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateChkObjects = _ZxAnSwAutoUpdateChkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1)
)


class _ZxAnSwAutoUpdateChkEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSwAutoUpdateChkEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkEnable_Object = MibScalar
zxAnSwAutoUpdateChkEnable = _ZxAnSwAutoUpdateChkEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 1),
    _ZxAnSwAutoUpdateChkEnable_Type()
)
zxAnSwAutoUpdateChkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkEnable.setStatus("current")
_ZxAnSwAutoUpdateChkStartTime_Type = DateAndTime
_ZxAnSwAutoUpdateChkStartTime_Object = MibScalar
zxAnSwAutoUpdateChkStartTime = _ZxAnSwAutoUpdateChkStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 2),
    _ZxAnSwAutoUpdateChkStartTime_Type()
)
zxAnSwAutoUpdateChkStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkStartTime.setStatus("current")


class _ZxAnSwAutoUpdateChkInterval_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnSwAutoUpdateChkInterval_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkInterval_Object = MibScalar
zxAnSwAutoUpdateChkInterval = _ZxAnSwAutoUpdateChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 3),
    _ZxAnSwAutoUpdateChkInterval_Type()
)
zxAnSwAutoUpdateChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkInterval.setUnits("hours")
_ZxAnSwAutoUpdateCurrChkStartTime_Type = DateAndTime
_ZxAnSwAutoUpdateCurrChkStartTime_Object = MibScalar
zxAnSwAutoUpdateCurrChkStartTime = _ZxAnSwAutoUpdateCurrChkStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 20),
    _ZxAnSwAutoUpdateCurrChkStartTime_Type()
)
zxAnSwAutoUpdateCurrChkStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrChkStartTime.setStatus("current")


class _ZxAnSwAutoUpdateChkDifferFiles_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateChkDifferFiles based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwAutoUpdateChkDifferFiles_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateChkDifferFiles_Object = MibScalar
zxAnSwAutoUpdateChkDifferFiles = _ZxAnSwAutoUpdateChkDifferFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 21),
    _ZxAnSwAutoUpdateChkDifferFiles_Type()
)
zxAnSwAutoUpdateChkDifferFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkDifferFiles.setStatus("current")


class _ZxAnSwAutoUpdateChkStatus_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnSwAutoUpdateChkStatus_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkStatus_Object = MibScalar
zxAnSwAutoUpdateChkStatus = _ZxAnSwAutoUpdateChkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 22),
    _ZxAnSwAutoUpdateChkStatus_Type()
)
zxAnSwAutoUpdateChkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkStatus.setStatus("current")


class _ZxAnSwAutoUpdateChkFailedReason_Type(Integer32):
    """Custom type zxAnSwAutoUpdateChkFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("fileServerUnconfigured", 2),
          ("fileServerConnectFailed", 3),
          ("fileServerLoginFailed", 4),
          ("fileServerPathError", 5),
          ("fileServerProtocolTypeError", 6),
          ("deviceCheckFailed", 7),
          ("otherErrors", 255))
    )


_ZxAnSwAutoUpdateChkFailedReason_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateChkFailedReason_Object = MibScalar
zxAnSwAutoUpdateChkFailedReason = _ZxAnSwAutoUpdateChkFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 1, 23),
    _ZxAnSwAutoUpdateChkFailedReason_Type()
)
zxAnSwAutoUpdateChkFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkFailedReason.setStatus("current")
_ZxAnSwAutoUpdateOperObjects_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateOperObjects = _ZxAnSwAutoUpdateOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2)
)


class _ZxAnSwAutoUpdateAction_Type(Integer32):
    """Custom type zxAnSwAutoUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_ZxAnSwAutoUpdateAction_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateAction_Object = MibScalar
zxAnSwAutoUpdateAction = _ZxAnSwAutoUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 1),
    _ZxAnSwAutoUpdateAction_Type()
)
zxAnSwAutoUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateAction.setStatus("current")


class _ZxAnSwAutoUpdateActiveEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateActiveEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSwAutoUpdateActiveEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateActiveEnable_Object = MibScalar
zxAnSwAutoUpdateActiveEnable = _ZxAnSwAutoUpdateActiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 2),
    _ZxAnSwAutoUpdateActiveEnable_Type()
)
zxAnSwAutoUpdateActiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateActiveEnable.setStatus("current")


class _ZxAnSwAutoUpdateSwBackupEnable_Type(Integer32):
    """Custom type zxAnSwAutoUpdateSwBackupEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSwAutoUpdateSwBackupEnable_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateSwBackupEnable_Object = MibScalar
zxAnSwAutoUpdateSwBackupEnable = _ZxAnSwAutoUpdateSwBackupEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 3),
    _ZxAnSwAutoUpdateSwBackupEnable_Type()
)
zxAnSwAutoUpdateSwBackupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateSwBackupEnable.setStatus("current")


class _ZxAnSwAutoUpdateStatus_Type(Integer32):
    """Custom type zxAnSwAutoUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("updateStarting", 2),
          ("backingUpFile", 3),
          ("versionFileAnalyzing", 4),
          ("versionFileDownloading", 5),
          ("versionFileDownloadComplete", 6),
          ("masterSlaveSynchronizing", 7),
          ("masterSlaveSyncComplete", 8),
          ("versionFileLoading", 9),
          ("bootUpdating", 10),
          ("bootUpdateComplete", 11),
          ("updateSuccess", 12),
          ("readyToReboot", 13),
          ("sameVersion", 14),
          ("updateFailed", 255))
    )


_ZxAnSwAutoUpdateStatus_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateStatus_Object = MibScalar
zxAnSwAutoUpdateStatus = _ZxAnSwAutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 20),
    _ZxAnSwAutoUpdateStatus_Type()
)
zxAnSwAutoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateStatus.setStatus("current")


class _ZxAnSwAutoUpdateCurrFileName_Type(DisplayString):
    """Custom type zxAnSwAutoUpdateCurrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwAutoUpdateCurrFileName_Type.__name__ = "DisplayString"
_ZxAnSwAutoUpdateCurrFileName_Object = MibScalar
zxAnSwAutoUpdateCurrFileName = _ZxAnSwAutoUpdateCurrFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 21),
    _ZxAnSwAutoUpdateCurrFileName_Type()
)
zxAnSwAutoUpdateCurrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileName.setStatus("current")
_ZxAnSwAutoUpdateCurrFileSize_Type = Integer32
_ZxAnSwAutoUpdateCurrFileSize_Object = MibScalar
zxAnSwAutoUpdateCurrFileSize = _ZxAnSwAutoUpdateCurrFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 22),
    _ZxAnSwAutoUpdateCurrFileSize_Type()
)
zxAnSwAutoUpdateCurrFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileSize.setUnits("bytes")


class _ZxAnSwAutoUpdateCurrFileProgress_Type(Integer32):
    """Custom type zxAnSwAutoUpdateCurrFileProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSwAutoUpdateCurrFileProgress_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateCurrFileProgress_Object = MibScalar
zxAnSwAutoUpdateCurrFileProgress = _ZxAnSwAutoUpdateCurrFileProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 23),
    _ZxAnSwAutoUpdateCurrFileProgress_Type()
)
zxAnSwAutoUpdateCurrFileProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateCurrFileProgress.setUnits("percent")
_ZxAnSwAutoUpdateTotalFiles_Type = Integer32
_ZxAnSwAutoUpdateTotalFiles_Object = MibScalar
zxAnSwAutoUpdateTotalFiles = _ZxAnSwAutoUpdateTotalFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 24),
    _ZxAnSwAutoUpdateTotalFiles_Type()
)
zxAnSwAutoUpdateTotalFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateTotalFiles.setStatus("current")
_ZxAnSwAutoUpdateSuccessFiles_Type = Integer32
_ZxAnSwAutoUpdateSuccessFiles_Object = MibScalar
zxAnSwAutoUpdateSuccessFiles = _ZxAnSwAutoUpdateSuccessFiles_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 25),
    _ZxAnSwAutoUpdateSuccessFiles_Type()
)
zxAnSwAutoUpdateSuccessFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateSuccessFiles.setStatus("current")


class _ZxAnSwAutoUpdateFailedReason_Type(Integer32):
    """Custom type zxAnSwAutoUpdateFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("backupDataError", 2),
          ("backupLogError", 3),
          ("backupConfigurationError", 4),
          ("backupVersionFileError", 5),
          ("backupOtherError", 6),
          ("analyzingConfigurationError", 7),
          ("analyzingVersionFileError", 8),
          ("diskFull", 9),
          ("downloadingVersionFileError", 10),
          ("updateVersionFileError", 11),
          ("updateBootError", 12),
          ("masterSlaveSynchronizeError", 13),
          ("updateConflict", 14),
          ("unavailableServer", 15),
          ("slaveCardNotInService", 16),
          ("fileNotExist", 17),
          ("otherErrors", 255))
    )


_ZxAnSwAutoUpdateFailedReason_Type.__name__ = "Integer32"
_ZxAnSwAutoUpdateFailedReason_Object = MibScalar
zxAnSwAutoUpdateFailedReason = _ZxAnSwAutoUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 3, 3, 1, 2, 26),
    _ZxAnSwAutoUpdateFailedReason_Type()
)
zxAnSwAutoUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateFailedReason.setStatus("current")
_ZxAnSwSwapObjects_ObjectIdentity = ObjectIdentity
zxAnSwSwapObjects = _ZxAnSwSwapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 4)
)
_ZxAnSwSwapGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSwSwapGlobalObjects = _ZxAnSwSwapGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 4, 1)
)
_ZxAnSwSwapRack_Type = Integer32
_ZxAnSwSwapRack_Object = MibScalar
zxAnSwSwapRack = _ZxAnSwSwapRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 4, 1, 1),
    _ZxAnSwSwapRack_Type()
)
zxAnSwSwapRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwSwapRack.setStatus("current")
_ZxAnSwSwapShelf_Type = Integer32
_ZxAnSwSwapShelf_Object = MibScalar
zxAnSwSwapShelf = _ZxAnSwSwapShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 4, 1, 2),
    _ZxAnSwSwapShelf_Type()
)
zxAnSwSwapShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwSwapShelf.setStatus("current")
_ZxAnSwSwapSlot_Type = Integer32
_ZxAnSwSwapSlot_Object = MibScalar
zxAnSwSwapSlot = _ZxAnSwSwapSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 4, 1, 3),
    _ZxAnSwSwapSlot_Type()
)
zxAnSwSwapSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwSwapSlot.setStatus("current")
_ZxAnCardPatchObjects_ObjectIdentity = ObjectIdentity
zxAnCardPatchObjects = _ZxAnCardPatchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5)
)
_ZxAnSwSavedPatchTable_Object = MibTable
zxAnSwSavedPatchTable = _ZxAnSwSavedPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchTable.setStatus("current")
_ZxAnSwSavedPatchEntry_Object = MibTableRow
zxAnSwSavedPatchEntry = _ZxAnSwSavedPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1)
)
zxAnSwSavedPatchEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchName"),
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchEntry.setStatus("current")
_ZxAnSwPatchRack_Type = Integer32
_ZxAnSwPatchRack_Object = MibTableColumn
zxAnSwPatchRack = _ZxAnSwPatchRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 1),
    _ZxAnSwPatchRack_Type()
)
zxAnSwPatchRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchRack.setStatus("current")
_ZxAnSwPatchShelf_Type = Integer32
_ZxAnSwPatchShelf_Object = MibTableColumn
zxAnSwPatchShelf = _ZxAnSwPatchShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 2),
    _ZxAnSwPatchShelf_Type()
)
zxAnSwPatchShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchShelf.setStatus("current")
_ZxAnSwPatchSlot_Type = Integer32
_ZxAnSwPatchSlot_Object = MibTableColumn
zxAnSwPatchSlot = _ZxAnSwPatchSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 3),
    _ZxAnSwPatchSlot_Type()
)
zxAnSwPatchSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchSlot.setStatus("current")


class _ZxAnSwPatchName_Type(DisplayString):
    """Custom type zxAnSwPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwPatchName_Type.__name__ = "DisplayString"
_ZxAnSwPatchName_Object = MibTableColumn
zxAnSwPatchName = _ZxAnSwPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 4),
    _ZxAnSwPatchName_Type()
)
zxAnSwPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchName.setStatus("current")


class _ZxAnSwPatchOwnerSwVersion_Type(DisplayString):
    """Custom type zxAnSwPatchOwnerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwPatchOwnerSwVersion_Type.__name__ = "DisplayString"
_ZxAnSwPatchOwnerSwVersion_Object = MibTableColumn
zxAnSwPatchOwnerSwVersion = _ZxAnSwPatchOwnerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 5),
    _ZxAnSwPatchOwnerSwVersion_Type()
)
zxAnSwPatchOwnerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchOwnerSwVersion.setStatus("current")


class _ZxAnSwPatchVersion_Type(DisplayString):
    """Custom type zxAnSwPatchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwPatchVersion_Type.__name__ = "DisplayString"
_ZxAnSwPatchVersion_Object = MibTableColumn
zxAnSwPatchVersion = _ZxAnSwPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 6),
    _ZxAnSwPatchVersion_Type()
)
zxAnSwPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchVersion.setStatus("current")
_ZxAnSwPatchSize_Type = Integer32
_ZxAnSwPatchSize_Object = MibTableColumn
zxAnSwPatchSize = _ZxAnSwPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 7),
    _ZxAnSwPatchSize_Type()
)
zxAnSwPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwPatchSize.setUnits("byte")
_ZxAnSwPatchBuildTime_Type = DateAndTime
_ZxAnSwPatchBuildTime_Object = MibTableColumn
zxAnSwPatchBuildTime = _ZxAnSwPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 8),
    _ZxAnSwPatchBuildTime_Type()
)
zxAnSwPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchBuildTime.setStatus("current")


class _ZxAnSwPatchConfActiveStatus_Type(Integer32):
    """Custom type zxAnSwPatchConfActiveStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_ZxAnSwPatchConfActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchConfActiveStatus_Object = MibTableColumn
zxAnSwPatchConfActiveStatus = _ZxAnSwPatchConfActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 9),
    _ZxAnSwPatchConfActiveStatus_Type()
)
zxAnSwPatchConfActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwPatchConfActiveStatus.setStatus("current")


class _ZxAnSwPatchDescription_Type(DisplayString):
    """Custom type zxAnSwPatchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwPatchDescription_Type.__name__ = "DisplayString"
_ZxAnSwPatchDescription_Object = MibTableColumn
zxAnSwPatchDescription = _ZxAnSwPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 2, 1, 10),
    _ZxAnSwPatchDescription_Type()
)
zxAnSwPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchDescription.setStatus("current")
_ZxAnSwCardPatchRunStatusTable_Object = MibTable
zxAnSwCardPatchRunStatusTable = _ZxAnSwCardPatchRunStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3)
)
if mibBuilder.loadTexts:
    zxAnSwCardPatchRunStatusTable.setStatus("current")
_ZxAnSwCardPatchRunStatusEntry_Object = MibTableRow
zxAnSwCardPatchRunStatusEntry = _ZxAnSwCardPatchRunStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1)
)
zxAnSwCardPatchRunStatusEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwCardPatchName"),
)
if mibBuilder.loadTexts:
    zxAnSwCardPatchRunStatusEntry.setStatus("current")


class _ZxAnSwCardPatchName_Type(DisplayString):
    """Custom type zxAnSwCardPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardPatchName_Type.__name__ = "DisplayString"
_ZxAnSwCardPatchName_Object = MibTableColumn
zxAnSwCardPatchName = _ZxAnSwCardPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 1),
    _ZxAnSwCardPatchName_Type()
)
zxAnSwCardPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwCardPatchName.setStatus("current")


class _ZxAnSwCardPatchOwnerSwVersion_Type(DisplayString):
    """Custom type zxAnSwCardPatchOwnerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardPatchOwnerSwVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardPatchOwnerSwVersion_Object = MibTableColumn
zxAnSwCardPatchOwnerSwVersion = _ZxAnSwCardPatchOwnerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 2),
    _ZxAnSwCardPatchOwnerSwVersion_Type()
)
zxAnSwCardPatchOwnerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchOwnerSwVersion.setStatus("current")


class _ZxAnSwCardPatchVersion_Type(DisplayString):
    """Custom type zxAnSwCardPatchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwCardPatchVersion_Type.__name__ = "DisplayString"
_ZxAnSwCardPatchVersion_Object = MibTableColumn
zxAnSwCardPatchVersion = _ZxAnSwCardPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 3),
    _ZxAnSwCardPatchVersion_Type()
)
zxAnSwCardPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchVersion.setStatus("current")
_ZxAnSwCardPatchSize_Type = Integer32
_ZxAnSwCardPatchSize_Object = MibTableColumn
zxAnSwCardPatchSize = _ZxAnSwCardPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 4),
    _ZxAnSwCardPatchSize_Type()
)
zxAnSwCardPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwCardPatchSize.setUnits("byte")
_ZxAnSwCardPatchBuildTime_Type = DateAndTime
_ZxAnSwCardPatchBuildTime_Object = MibTableColumn
zxAnSwCardPatchBuildTime = _ZxAnSwCardPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 5),
    _ZxAnSwCardPatchBuildTime_Type()
)
zxAnSwCardPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchBuildTime.setStatus("current")
_ZxAnSwCardPatchActivatedTime_Type = DateAndTime
_ZxAnSwCardPatchActivatedTime_Object = MibTableColumn
zxAnSwCardPatchActivatedTime = _ZxAnSwCardPatchActivatedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 6),
    _ZxAnSwCardPatchActivatedTime_Type()
)
zxAnSwCardPatchActivatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchActivatedTime.setStatus("current")


class _ZxAnSwCardPatchDescription_Type(DisplayString):
    """Custom type zxAnSwCardPatchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwCardPatchDescription_Type.__name__ = "DisplayString"
_ZxAnSwCardPatchDescription_Object = MibTableColumn
zxAnSwCardPatchDescription = _ZxAnSwCardPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 7),
    _ZxAnSwCardPatchDescription_Type()
)
zxAnSwCardPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchDescription.setStatus("current")


class _ZxAnSwCardPatchRunningStatus_Type(Integer32):
    """Custom type zxAnSwCardPatchRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activatingSucceeded", 1),
          ("activatingFailed", 2),
          ("waitingToBeActivated", 3),
          ("resettingCardNeeded", 4),
          ("mismatched", 5))
    )


_ZxAnSwCardPatchRunningStatus_Type.__name__ = "Integer32"
_ZxAnSwCardPatchRunningStatus_Object = MibTableColumn
zxAnSwCardPatchRunningStatus = _ZxAnSwCardPatchRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 3, 1, 8),
    _ZxAnSwCardPatchRunningStatus_Type()
)
zxAnSwCardPatchRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwCardPatchRunningStatus.setStatus("current")
_ZxAnSwSubcardRunningPatchTable_Object = MibTable
zxAnSwSubcardRunningPatchTable = _ZxAnSwSubcardRunningPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4)
)
if mibBuilder.loadTexts:
    zxAnSwSubcardRunningPatchTable.setStatus("current")
_ZxAnSwSubcardRunningPatchEntry_Object = MibTableRow
zxAnSwSubcardRunningPatchEntry = _ZxAnSwSubcardRunningPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1)
)
zxAnSwSubcardRunningPatchEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSubcardSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardPatchName"),
)
if mibBuilder.loadTexts:
    zxAnSwSubcardRunningPatchEntry.setStatus("current")
_ZxAnSwPatchSubcardSlot_Type = Integer32
_ZxAnSwPatchSubcardSlot_Object = MibTableColumn
zxAnSwPatchSubcardSlot = _ZxAnSwPatchSubcardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 1),
    _ZxAnSwPatchSubcardSlot_Type()
)
zxAnSwPatchSubcardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchSubcardSlot.setStatus("current")


class _ZxAnSwSubcardPatchName_Type(DisplayString):
    """Custom type zxAnSwSubcardPatchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardPatchName_Type.__name__ = "DisplayString"
_ZxAnSwSubcardPatchName_Object = MibTableColumn
zxAnSwSubcardPatchName = _ZxAnSwSubcardPatchName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 2),
    _ZxAnSwSubcardPatchName_Type()
)
zxAnSwSubcardPatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchName.setStatus("current")


class _ZxAnSwSubcardPatchOwnerSwVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardPatchOwnerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardPatchOwnerSwVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardPatchOwnerSwVersion_Object = MibTableColumn
zxAnSwSubcardPatchOwnerSwVersion = _ZxAnSwSubcardPatchOwnerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 3),
    _ZxAnSwSubcardPatchOwnerSwVersion_Type()
)
zxAnSwSubcardPatchOwnerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchOwnerSwVersion.setStatus("current")


class _ZxAnSwSubcardPatchVersion_Type(DisplayString):
    """Custom type zxAnSwSubcardPatchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwSubcardPatchVersion_Type.__name__ = "DisplayString"
_ZxAnSwSubcardPatchVersion_Object = MibTableColumn
zxAnSwSubcardPatchVersion = _ZxAnSwSubcardPatchVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 4),
    _ZxAnSwSubcardPatchVersion_Type()
)
zxAnSwSubcardPatchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchVersion.setStatus("current")
_ZxAnSwSubcardPatchSize_Type = Integer32
_ZxAnSwSubcardPatchSize_Object = MibTableColumn
zxAnSwSubcardPatchSize = _ZxAnSwSubcardPatchSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 5),
    _ZxAnSwSubcardPatchSize_Type()
)
zxAnSwSubcardPatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchSize.setUnits("byte")
_ZxAnSwSubcardPatchBuildTime_Type = DateAndTime
_ZxAnSwSubcardPatchBuildTime_Object = MibTableColumn
zxAnSwSubcardPatchBuildTime = _ZxAnSwSubcardPatchBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 6),
    _ZxAnSwSubcardPatchBuildTime_Type()
)
zxAnSwSubcardPatchBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchBuildTime.setStatus("current")
_ZxAnSwSubcardPatchActivatedTime_Type = DateAndTime
_ZxAnSwSubcardPatchActivatedTime_Object = MibTableColumn
zxAnSwSubcardPatchActivatedTime = _ZxAnSwSubcardPatchActivatedTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 7),
    _ZxAnSwSubcardPatchActivatedTime_Type()
)
zxAnSwSubcardPatchActivatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchActivatedTime.setStatus("current")


class _ZxAnSwSubcardPatchDescription_Type(DisplayString):
    """Custom type zxAnSwSubcardPatchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwSubcardPatchDescription_Type.__name__ = "DisplayString"
_ZxAnSwSubcardPatchDescription_Object = MibTableColumn
zxAnSwSubcardPatchDescription = _ZxAnSwSubcardPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 4, 1, 8),
    _ZxAnSwSubcardPatchDescription_Type()
)
zxAnSwSubcardPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwSubcardPatchDescription.setStatus("current")
_ZxAnSwSavedPatchPackageTable_Object = MibTable
zxAnSwSavedPatchPackageTable = _ZxAnSwSavedPatchPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5)
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchPackageTable.setStatus("current")
_ZxAnSwSavedPatchPackageEntry_Object = MibTableRow
zxAnSwSavedPatchPackageEntry = _ZxAnSwSavedPatchPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1)
)
zxAnSwSavedPatchPackageEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchPkgName"),
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchPackageEntry.setStatus("current")


class _ZxAnSwPatchPkgName_Type(DisplayString):
    """Custom type zxAnSwPatchPkgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwPatchPkgName_Type.__name__ = "DisplayString"
_ZxAnSwPatchPkgName_Object = MibTableColumn
zxAnSwPatchPkgName = _ZxAnSwPatchPkgName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 1),
    _ZxAnSwPatchPkgName_Type()
)
zxAnSwPatchPkgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgName.setStatus("current")


class _ZxAnSwPatchPkgVersion_Type(DisplayString):
    """Custom type zxAnSwPatchPkgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSwPatchPkgVersion_Type.__name__ = "DisplayString"
_ZxAnSwPatchPkgVersion_Object = MibTableColumn
zxAnSwPatchPkgVersion = _ZxAnSwPatchPkgVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 2),
    _ZxAnSwPatchPkgVersion_Type()
)
zxAnSwPatchPkgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgVersion.setStatus("current")
_ZxAnSwPatchPkgSize_Type = Integer32
_ZxAnSwPatchPkgSize_Object = MibTableColumn
zxAnSwPatchPkgSize = _ZxAnSwPatchPkgSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 3),
    _ZxAnSwPatchPkgSize_Type()
)
zxAnSwPatchPkgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgSize.setUnits("byte")
_ZxAnSwPatchPkgBuildTime_Type = DateAndTime
_ZxAnSwPatchPkgBuildTime_Object = MibTableColumn
zxAnSwPatchPkgBuildTime = _ZxAnSwPatchPkgBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 4),
    _ZxAnSwPatchPkgBuildTime_Type()
)
zxAnSwPatchPkgBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgBuildTime.setStatus("current")


class _ZxAnSwPatchPkgDescription_Type(DisplayString):
    """Custom type zxAnSwPatchPkgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnSwPatchPkgDescription_Type.__name__ = "DisplayString"
_ZxAnSwPatchPkgDescription_Object = MibTableColumn
zxAnSwPatchPkgDescription = _ZxAnSwPatchPkgDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 5),
    _ZxAnSwPatchPkgDescription_Type()
)
zxAnSwPatchPkgDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgDescription.setStatus("current")


class _ZxAnSwPatchPkgConfActiveStatus_Type(Integer32):
    """Custom type zxAnSwPatchPkgConfActiveStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_ZxAnSwPatchPkgConfActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchPkgConfActiveStatus_Object = MibTableColumn
zxAnSwPatchPkgConfActiveStatus = _ZxAnSwPatchPkgConfActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 6),
    _ZxAnSwPatchPkgConfActiveStatus_Type()
)
zxAnSwPatchPkgConfActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgConfActiveStatus.setStatus("current")


class _ZxAnSwPatchPkgActualActiveStatus_Type(Integer32):
    """Custom type zxAnSwPatchPkgActualActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_ZxAnSwPatchPkgActualActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchPkgActualActiveStatus_Object = MibTableColumn
zxAnSwPatchPkgActualActiveStatus = _ZxAnSwPatchPkgActualActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 5, 1, 7),
    _ZxAnSwPatchPkgActualActiveStatus_Type()
)
zxAnSwPatchPkgActualActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgActualActiveStatus.setStatus("current")
_ZxAnSwSavedPatchPackageFileTable_Object = MibTable
zxAnSwSavedPatchPackageFileTable = _ZxAnSwSavedPatchPackageFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6)
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchPackageFileTable.setStatus("current")
_ZxAnSwSavedPatchPackageFileEntry_Object = MibTableRow
zxAnSwSavedPatchPackageFileEntry = _ZxAnSwSavedPatchPackageFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6, 1)
)
zxAnSwSavedPatchPackageFileEntry.setIndexNames(
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchRack"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchShelf"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchSlot"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchPkgName"),
    (0, "ZTE-AN-SOFTWARE-MIB", "zxAnSwPatchPkgFileName"),
)
if mibBuilder.loadTexts:
    zxAnSwSavedPatchPackageFileEntry.setStatus("current")


class _ZxAnSwPatchPkgFileName_Type(DisplayString):
    """Custom type zxAnSwPatchPkgFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSwPatchPkgFileName_Type.__name__ = "DisplayString"
_ZxAnSwPatchPkgFileName_Object = MibTableColumn
zxAnSwPatchPkgFileName = _ZxAnSwPatchPkgFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6, 1, 1),
    _ZxAnSwPatchPkgFileName_Type()
)
zxAnSwPatchPkgFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgFileName.setStatus("current")
_ZxAnSwPatchPkgFileBuildTime_Type = DateAndTime
_ZxAnSwPatchPkgFileBuildTime_Object = MibTableColumn
zxAnSwPatchPkgFileBuildTime = _ZxAnSwPatchPkgFileBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6, 1, 2),
    _ZxAnSwPatchPkgFileBuildTime_Type()
)
zxAnSwPatchPkgFileBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgFileBuildTime.setStatus("current")


class _ZxAnSwPatchPkgFileNeedResetCard_Type(Integer32):
    """Custom type zxAnSwPatchPkgFileNeedResetCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_ZxAnSwPatchPkgFileNeedResetCard_Type.__name__ = "Integer32"
_ZxAnSwPatchPkgFileNeedResetCard_Object = MibTableColumn
zxAnSwPatchPkgFileNeedResetCard = _ZxAnSwPatchPkgFileNeedResetCard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6, 1, 3),
    _ZxAnSwPatchPkgFileNeedResetCard_Type()
)
zxAnSwPatchPkgFileNeedResetCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgFileNeedResetCard.setStatus("current")


class _ZxAnSwPatchPkgFileActiveStatus_Type(Integer32):
    """Custom type zxAnSwPatchPkgFileActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_ZxAnSwPatchPkgFileActiveStatus_Type.__name__ = "Integer32"
_ZxAnSwPatchPkgFileActiveStatus_Object = MibTableColumn
zxAnSwPatchPkgFileActiveStatus = _ZxAnSwPatchPkgFileActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 2, 5, 6, 1, 4),
    _ZxAnSwPatchPkgFileActiveStatus_Type()
)
zxAnSwPatchPkgFileActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSwPatchPkgFileActiveStatus.setStatus("current")
_ZxAnSwNotifications_ObjectIdentity = ObjectIdentity
zxAnSwNotifications = _ZxAnSwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 3)
)
_ZxAnSwAutoUpdateTraps_ObjectIdentity = ObjectIdentity
zxAnSwAutoUpdateTraps = _ZxAnSwAutoUpdateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 3, 1)
)
_ZxAnSwConformance_ObjectIdentity = ObjectIdentity
zxAnSwConformance = _ZxAnSwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4)
)
_ZxAnSwCompliances_ObjectIdentity = ObjectIdentity
zxAnSwCompliances = _ZxAnSwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 1)
)
_ZxAnSwGroups_ObjectIdentity = ObjectIdentity
zxAnSwGroups = _ZxAnSwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2)
)

# Managed Objects groups

zxAnSwCardRunVerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 1)
)
zxAnSwCardRunVerGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBootwareFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBootwareFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBootwareVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBootwareFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardBootwareBuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware1FileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware1FileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware1Version"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware1FileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware1BuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware2FileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware2FileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware2Version"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware2FileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware2BuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware3FileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware3FileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware3Version"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware3FileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardFirmware3BuildTime"))
)
if mibBuilder.loadTexts:
    zxAnSwCardRunVerGroup.setStatus("current")

zxAnSwSubcardRunVerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 2)
)
zxAnSwSubcardRunVerGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBootwareFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBootwareFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBootwareVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBootwareFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardBootwareBuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFirmwareFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFirmwareFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFirmwareVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFirmwareFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardFirmwareBuildTime"))
)
if mibBuilder.loadTexts:
    zxAnSwSubcardRunVerGroup.setStatus("current")

zxAnSwImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 3)
)
zxAnSwImageGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageFileType"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageVersion"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageFileLen"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageBuildTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageActiveStatus"))
)
if mibBuilder.loadTexts:
    zxAnSwImageGroup.setStatus("current")

zxAnSwManualUpdateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 4)
)
zxAnSwManualUpdateGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateRack"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateShelf"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateSlotList"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateSwType"))
)
if mibBuilder.loadTexts:
    zxAnSwManualUpdateGroup.setStatus("current")

zxAnSwManualUpdateStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 5)
)
zxAnSwManualUpdateStatusGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateStatus"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwManualUpdateStatusGroup.setStatus("current")

zxAnSwAutoUpdateChkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 6)
)
zxAnSwAutoUpdateChkGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkEnable"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkStartTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkInterval"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrChkStartTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkDifferFiles"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkStatus"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateChkGroup.setStatus("current")

zxAnSwAutoUpdateOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 7)
)
zxAnSwAutoUpdateOperGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateAction"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateActiveEnable"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateSwBackupEnable"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateStatus"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrFileName"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrFileSize"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrFileProgress"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateTotalFiles"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateSuccessFiles"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateOperGroup.setStatus("current")

zxAnSwSwapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 8)
)
zxAnSwSwapGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwSwapRack"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSwapShelf"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSwapSlot"))
)
if mibBuilder.loadTexts:
    zxAnSwSwapGroup.setStatus("current")

zxAnSwNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 2, 9)
)
zxAnSwNotificationsGroup.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateFinished"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateSwDiffer"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateSwChkFailed"))
)
if mibBuilder.loadTexts:
    zxAnSwNotificationsGroup.setStatus("current")


# Notification objects

zxAnSwAutoUpdateFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 3, 1, 1)
)
zxAnSwAutoUpdateFinished.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateStatus"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateFinished.setStatus(
        "current"
    )

zxAnSwAutoUpdateSwDiffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 3, 1, 2)
)
zxAnSwAutoUpdateSwDiffer.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrChkStartTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkDifferFiles"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateSwDiffer.setStatus(
        "current"
    )

zxAnSwAutoUpdateSwChkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 3, 1, 3)
)
zxAnSwAutoUpdateSwChkFailed.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateCurrChkStartTime"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnSwAutoUpdateSwChkFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnSwCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 20, 30, 4, 1, 1)
)
zxAnSwCompliance.setObjects(
      *(("ZTE-AN-SOFTWARE-MIB", "zxAnSwCardRunVerGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSubcardRunVerGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwImageGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwManualUpdateStatusGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateChkGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwAutoUpdateOperGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwSwapGroup"),
        ("ZTE-AN-SOFTWARE-MIB", "zxAnSwNotificationsGroup"))
)
if mibBuilder.loadTexts:
    zxAnSwCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SOFTWARE-MIB",
    **{"zxAnSoftwareMib": zxAnSoftwareMib,
       "zxAnSwObjects": zxAnSwObjects,
       "zxAnCardSwObjects": zxAnCardSwObjects,
       "zxAnSwCardRunningVerTable": zxAnSwCardRunningVerTable,
       "zxAnSwCardRunningVerEntry": zxAnSwCardRunningVerEntry,
       "zxAnSwCardRack": zxAnSwCardRack,
       "zxAnSwCardShelf": zxAnSwCardShelf,
       "zxAnSwCardSlot": zxAnSwCardSlot,
       "zxAnSwCardFileName": zxAnSwCardFileName,
       "zxAnSwCardFileType": zxAnSwCardFileType,
       "zxAnSwCardVersion": zxAnSwCardVersion,
       "zxAnSwCardFileLen": zxAnSwCardFileLen,
       "zxAnSwCardBuildTime": zxAnSwCardBuildTime,
       "zxAnSwCardBootwareFileName": zxAnSwCardBootwareFileName,
       "zxAnSwCardBootwareFileType": zxAnSwCardBootwareFileType,
       "zxAnSwCardBootwareVersion": zxAnSwCardBootwareVersion,
       "zxAnSwCardBootwareFileLen": zxAnSwCardBootwareFileLen,
       "zxAnSwCardBootwareBuildTime": zxAnSwCardBootwareBuildTime,
       "zxAnSwCardFirmware1FileName": zxAnSwCardFirmware1FileName,
       "zxAnSwCardFirmware1FileType": zxAnSwCardFirmware1FileType,
       "zxAnSwCardFirmware1Version": zxAnSwCardFirmware1Version,
       "zxAnSwCardFirmware1FileLen": zxAnSwCardFirmware1FileLen,
       "zxAnSwCardFirmware1BuildTime": zxAnSwCardFirmware1BuildTime,
       "zxAnSwCardFirmware2FileName": zxAnSwCardFirmware2FileName,
       "zxAnSwCardFirmware2FileType": zxAnSwCardFirmware2FileType,
       "zxAnSwCardFirmware2Version": zxAnSwCardFirmware2Version,
       "zxAnSwCardFirmware2FileLen": zxAnSwCardFirmware2FileLen,
       "zxAnSwCardFirmware2BuildTime": zxAnSwCardFirmware2BuildTime,
       "zxAnSwCardFirmware3FileName": zxAnSwCardFirmware3FileName,
       "zxAnSwCardFirmware3FileType": zxAnSwCardFirmware3FileType,
       "zxAnSwCardFirmware3Version": zxAnSwCardFirmware3Version,
       "zxAnSwCardFirmware3FileLen": zxAnSwCardFirmware3FileLen,
       "zxAnSwCardFirmware3BuildTime": zxAnSwCardFirmware3BuildTime,
       "zxAnSwSubcardRunningVerTable": zxAnSwSubcardRunningVerTable,
       "zxAnSwSubcardRunningVerEntry": zxAnSwSubcardRunningVerEntry,
       "zxAnSwSubcardSlot": zxAnSwSubcardSlot,
       "zxAnSwSubcardFileName": zxAnSwSubcardFileName,
       "zxAnSwSubcardFileType": zxAnSwSubcardFileType,
       "zxAnSwSubcardVersion": zxAnSwSubcardVersion,
       "zxAnSwSubcardFileLen": zxAnSwSubcardFileLen,
       "zxAnSwSubcardBuildTime": zxAnSwSubcardBuildTime,
       "zxAnSwSubcardBootwareFileName": zxAnSwSubcardBootwareFileName,
       "zxAnSwSubcardBootwareFileType": zxAnSwSubcardBootwareFileType,
       "zxAnSwSubcardBootwareVersion": zxAnSwSubcardBootwareVersion,
       "zxAnSwSubcardBootwareFileLen": zxAnSwSubcardBootwareFileLen,
       "zxAnSwSubcardBootwareBuildTime": zxAnSwSubcardBootwareBuildTime,
       "zxAnSwSubcardFirmwareFileName": zxAnSwSubcardFirmwareFileName,
       "zxAnSwSubcardFirmwareFileType": zxAnSwSubcardFirmwareFileType,
       "zxAnSwSubcardFirmwareVersion": zxAnSwSubcardFirmwareVersion,
       "zxAnSwSubcardFirmwareFileLen": zxAnSwSubcardFirmwareFileLen,
       "zxAnSwSubcardFirmwareBuildTime": zxAnSwSubcardFirmwareBuildTime,
       "zxAnSwImageTable": zxAnSwImageTable,
       "zxAnSwImageEntry": zxAnSwImageEntry,
       "zxAnSwImageFileName": zxAnSwImageFileName,
       "zxAnSwImageFileType": zxAnSwImageFileType,
       "zxAnSwImageVersion": zxAnSwImageVersion,
       "zxAnSwImageFileLen": zxAnSwImageFileLen,
       "zxAnSwImageBuildTime": zxAnSwImageBuildTime,
       "zxAnSwImageActiveStatus": zxAnSwImageActiveStatus,
       "zxAnSwImageDownloadTime": zxAnSwImageDownloadTime,
       "zxAnSwUpdateObjects": zxAnSwUpdateObjects,
       "zxAnSwManualUpdateObjects": zxAnSwManualUpdateObjects,
       "zxAnSwManualUpdateGlobalObjects": zxAnSwManualUpdateGlobalObjects,
       "zxAnSwManualUpdateRack": zxAnSwManualUpdateRack,
       "zxAnSwManualUpdateShelf": zxAnSwManualUpdateShelf,
       "zxAnSwManualUpdateSlotList": zxAnSwManualUpdateSlotList,
       "zxAnSwManualUpdateSwType": zxAnSwManualUpdateSwType,
       "zxAnSwManualUpdateSubcardList": zxAnSwManualUpdateSubcardList,
       "zxAnSwManualUpdateStatusTable": zxAnSwManualUpdateStatusTable,
       "zxAnSwManualUpdateStatusEntry": zxAnSwManualUpdateStatusEntry,
       "zxAnSwManualUpdateSoftwareType": zxAnSwManualUpdateSoftwareType,
       "zxAnSwManualUpdateStatus": zxAnSwManualUpdateStatus,
       "zxAnSwManualFailedReason": zxAnSwManualFailedReason,
       "zxAnSwSubcardMUpdateStatusTable": zxAnSwSubcardMUpdateStatusTable,
       "zxAnSwSubcardMUpdateStatusEntry": zxAnSwSubcardMUpdateStatusEntry,
       "zxAnSwSubcardMUpdateSoftwareType": zxAnSwSubcardMUpdateSoftwareType,
       "zxAnSwSubcardMUpdateStatus": zxAnSwSubcardMUpdateStatus,
       "zxAnSwSubcardMUpdateFailedReason": zxAnSwSubcardMUpdateFailedReason,
       "zxAnSwAutoUpdateObjects": zxAnSwAutoUpdateObjects,
       "zxAnSwAutoUpdateGlobalObjects": zxAnSwAutoUpdateGlobalObjects,
       "zxAnSwAutoUpdateChkObjects": zxAnSwAutoUpdateChkObjects,
       "zxAnSwAutoUpdateChkEnable": zxAnSwAutoUpdateChkEnable,
       "zxAnSwAutoUpdateChkStartTime": zxAnSwAutoUpdateChkStartTime,
       "zxAnSwAutoUpdateChkInterval": zxAnSwAutoUpdateChkInterval,
       "zxAnSwAutoUpdateCurrChkStartTime": zxAnSwAutoUpdateCurrChkStartTime,
       "zxAnSwAutoUpdateChkDifferFiles": zxAnSwAutoUpdateChkDifferFiles,
       "zxAnSwAutoUpdateChkStatus": zxAnSwAutoUpdateChkStatus,
       "zxAnSwAutoUpdateChkFailedReason": zxAnSwAutoUpdateChkFailedReason,
       "zxAnSwAutoUpdateOperObjects": zxAnSwAutoUpdateOperObjects,
       "zxAnSwAutoUpdateAction": zxAnSwAutoUpdateAction,
       "zxAnSwAutoUpdateActiveEnable": zxAnSwAutoUpdateActiveEnable,
       "zxAnSwAutoUpdateSwBackupEnable": zxAnSwAutoUpdateSwBackupEnable,
       "zxAnSwAutoUpdateStatus": zxAnSwAutoUpdateStatus,
       "zxAnSwAutoUpdateCurrFileName": zxAnSwAutoUpdateCurrFileName,
       "zxAnSwAutoUpdateCurrFileSize": zxAnSwAutoUpdateCurrFileSize,
       "zxAnSwAutoUpdateCurrFileProgress": zxAnSwAutoUpdateCurrFileProgress,
       "zxAnSwAutoUpdateTotalFiles": zxAnSwAutoUpdateTotalFiles,
       "zxAnSwAutoUpdateSuccessFiles": zxAnSwAutoUpdateSuccessFiles,
       "zxAnSwAutoUpdateFailedReason": zxAnSwAutoUpdateFailedReason,
       "zxAnSwSwapObjects": zxAnSwSwapObjects,
       "zxAnSwSwapGlobalObjects": zxAnSwSwapGlobalObjects,
       "zxAnSwSwapRack": zxAnSwSwapRack,
       "zxAnSwSwapShelf": zxAnSwSwapShelf,
       "zxAnSwSwapSlot": zxAnSwSwapSlot,
       "zxAnCardPatchObjects": zxAnCardPatchObjects,
       "zxAnSwSavedPatchTable": zxAnSwSavedPatchTable,
       "zxAnSwSavedPatchEntry": zxAnSwSavedPatchEntry,
       "zxAnSwPatchRack": zxAnSwPatchRack,
       "zxAnSwPatchShelf": zxAnSwPatchShelf,
       "zxAnSwPatchSlot": zxAnSwPatchSlot,
       "zxAnSwPatchName": zxAnSwPatchName,
       "zxAnSwPatchOwnerSwVersion": zxAnSwPatchOwnerSwVersion,
       "zxAnSwPatchVersion": zxAnSwPatchVersion,
       "zxAnSwPatchSize": zxAnSwPatchSize,
       "zxAnSwPatchBuildTime": zxAnSwPatchBuildTime,
       "zxAnSwPatchConfActiveStatus": zxAnSwPatchConfActiveStatus,
       "zxAnSwPatchDescription": zxAnSwPatchDescription,
       "zxAnSwCardPatchRunStatusTable": zxAnSwCardPatchRunStatusTable,
       "zxAnSwCardPatchRunStatusEntry": zxAnSwCardPatchRunStatusEntry,
       "zxAnSwCardPatchName": zxAnSwCardPatchName,
       "zxAnSwCardPatchOwnerSwVersion": zxAnSwCardPatchOwnerSwVersion,
       "zxAnSwCardPatchVersion": zxAnSwCardPatchVersion,
       "zxAnSwCardPatchSize": zxAnSwCardPatchSize,
       "zxAnSwCardPatchBuildTime": zxAnSwCardPatchBuildTime,
       "zxAnSwCardPatchActivatedTime": zxAnSwCardPatchActivatedTime,
       "zxAnSwCardPatchDescription": zxAnSwCardPatchDescription,
       "zxAnSwCardPatchRunningStatus": zxAnSwCardPatchRunningStatus,
       "zxAnSwSubcardRunningPatchTable": zxAnSwSubcardRunningPatchTable,
       "zxAnSwSubcardRunningPatchEntry": zxAnSwSubcardRunningPatchEntry,
       "zxAnSwPatchSubcardSlot": zxAnSwPatchSubcardSlot,
       "zxAnSwSubcardPatchName": zxAnSwSubcardPatchName,
       "zxAnSwSubcardPatchOwnerSwVersion": zxAnSwSubcardPatchOwnerSwVersion,
       "zxAnSwSubcardPatchVersion": zxAnSwSubcardPatchVersion,
       "zxAnSwSubcardPatchSize": zxAnSwSubcardPatchSize,
       "zxAnSwSubcardPatchBuildTime": zxAnSwSubcardPatchBuildTime,
       "zxAnSwSubcardPatchActivatedTime": zxAnSwSubcardPatchActivatedTime,
       "zxAnSwSubcardPatchDescription": zxAnSwSubcardPatchDescription,
       "zxAnSwSavedPatchPackageTable": zxAnSwSavedPatchPackageTable,
       "zxAnSwSavedPatchPackageEntry": zxAnSwSavedPatchPackageEntry,
       "zxAnSwPatchPkgName": zxAnSwPatchPkgName,
       "zxAnSwPatchPkgVersion": zxAnSwPatchPkgVersion,
       "zxAnSwPatchPkgSize": zxAnSwPatchPkgSize,
       "zxAnSwPatchPkgBuildTime": zxAnSwPatchPkgBuildTime,
       "zxAnSwPatchPkgDescription": zxAnSwPatchPkgDescription,
       "zxAnSwPatchPkgConfActiveStatus": zxAnSwPatchPkgConfActiveStatus,
       "zxAnSwPatchPkgActualActiveStatus": zxAnSwPatchPkgActualActiveStatus,
       "zxAnSwSavedPatchPackageFileTable": zxAnSwSavedPatchPackageFileTable,
       "zxAnSwSavedPatchPackageFileEntry": zxAnSwSavedPatchPackageFileEntry,
       "zxAnSwPatchPkgFileName": zxAnSwPatchPkgFileName,
       "zxAnSwPatchPkgFileBuildTime": zxAnSwPatchPkgFileBuildTime,
       "zxAnSwPatchPkgFileNeedResetCard": zxAnSwPatchPkgFileNeedResetCard,
       "zxAnSwPatchPkgFileActiveStatus": zxAnSwPatchPkgFileActiveStatus,
       "zxAnSwNotifications": zxAnSwNotifications,
       "zxAnSwAutoUpdateTraps": zxAnSwAutoUpdateTraps,
       "zxAnSwAutoUpdateFinished": zxAnSwAutoUpdateFinished,
       "zxAnSwAutoUpdateSwDiffer": zxAnSwAutoUpdateSwDiffer,
       "zxAnSwAutoUpdateSwChkFailed": zxAnSwAutoUpdateSwChkFailed,
       "zxAnSwConformance": zxAnSwConformance,
       "zxAnSwCompliances": zxAnSwCompliances,
       "zxAnSwCompliance": zxAnSwCompliance,
       "zxAnSwGroups": zxAnSwGroups,
       "zxAnSwCardRunVerGroup": zxAnSwCardRunVerGroup,
       "zxAnSwSubcardRunVerGroup": zxAnSwSubcardRunVerGroup,
       "zxAnSwImageGroup": zxAnSwImageGroup,
       "zxAnSwManualUpdateGroup": zxAnSwManualUpdateGroup,
       "zxAnSwManualUpdateStatusGroup": zxAnSwManualUpdateStatusGroup,
       "zxAnSwAutoUpdateChkGroup": zxAnSwAutoUpdateChkGroup,
       "zxAnSwAutoUpdateOperGroup": zxAnSwAutoUpdateOperGroup,
       "zxAnSwSwapGroup": zxAnSwSwapGroup,
       "zxAnSwNotificationsGroup": zxAnSwNotificationsGroup}
)
