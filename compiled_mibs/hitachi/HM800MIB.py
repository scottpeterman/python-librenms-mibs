# SNMP MIB module (HM800MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hitachi\HM800MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:29 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hitachi_ObjectIdentity = ObjectIdentity
hitachi = _Hitachi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11)
)
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4)
)
_RaidDummy_ObjectIdentity = ObjectIdentity
raidDummy = _RaidDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1)
)
_RaidRoot_ObjectIdentity = ObjectIdentity
raidRoot = _RaidRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1)
)
_SystemExMib_ObjectIdentity = ObjectIdentity
systemExMib = _SystemExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5)
)
_StorageExMib_ObjectIdentity = ObjectIdentity
storageExMib = _StorageExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11)
)
_RaidExMib_ObjectIdentity = ObjectIdentity
raidExMib = _RaidExMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4)
)
_RaidExMibDummy_ObjectIdentity = ObjectIdentity
raidExMibDummy = _RaidExMibDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1)
)
_RaidExMibRoot_ObjectIdentity = ObjectIdentity
raidExMibRoot = _RaidExMibRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1)
)
_RaidExMibName_Type = DisplayString
_RaidExMibName_Object = MibScalar
raidExMibName = _RaidExMibName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 1),
    _RaidExMibName_Type()
)
raidExMibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibName.setStatus("mandatory")
_RaidExMibVersion_Type = DisplayString
_RaidExMibVersion_Object = MibScalar
raidExMibVersion = _RaidExMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 2),
    _RaidExMibVersion_Type()
)
raidExMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibVersion.setStatus("mandatory")
_RaidExMibAgentVersion_Type = DisplayString
_RaidExMibAgentVersion_Object = MibScalar
raidExMibAgentVersion = _RaidExMibAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 3),
    _RaidExMibAgentVersion_Type()
)
raidExMibAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibAgentVersion.setStatus("mandatory")
_RaidExMibDkcCount_Type = Integer32
_RaidExMibDkcCount_Object = MibScalar
raidExMibDkcCount = _RaidExMibDkcCount_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 4),
    _RaidExMibDkcCount_Type()
)
raidExMibDkcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidExMibDkcCount.setStatus("mandatory")
_RaidExMibRaidListTable_Object = MibTable
raidExMibRaidListTable = _RaidExMibRaidListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    raidExMibRaidListTable.setStatus("mandatory")
_RaidExMibRaidListEntry_Object = MibTableRow
raidExMibRaidListEntry = _RaidExMibRaidListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1)
)
raidExMibRaidListEntry.setIndexNames(
    (0, "HM800MIB", "raidlistSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibRaidListEntry.setStatus("mandatory")
_RaidlistSerialNumber_Type = Integer32
_RaidlistSerialNumber_Object = MibTableColumn
raidlistSerialNumber = _RaidlistSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 1),
    _RaidlistSerialNumber_Type()
)
raidlistSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistSerialNumber.setStatus("mandatory")


class _RaidlistMibNickName_Type(DisplayString):
    """Custom type raidlistMibNickName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_RaidlistMibNickName_Type.__name__ = "DisplayString"
_RaidlistMibNickName_Object = MibTableColumn
raidlistMibNickName = _RaidlistMibNickName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 2),
    _RaidlistMibNickName_Type()
)
raidlistMibNickName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistMibNickName.setStatus("mandatory")
_RaidlistDKCMainVersion_Type = DisplayString
_RaidlistDKCMainVersion_Object = MibTableColumn
raidlistDKCMainVersion = _RaidlistDKCMainVersion_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 3),
    _RaidlistDKCMainVersion_Type()
)
raidlistDKCMainVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistDKCMainVersion.setStatus("mandatory")
_RaidlistDKCProductName_Type = DisplayString
_RaidlistDKCProductName_Object = MibTableColumn
raidlistDKCProductName = _RaidlistDKCProductName_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 5, 1, 4),
    _RaidlistDKCProductName_Type()
)
raidlistDKCProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidlistDKCProductName.setStatus("mandatory")
_RaidExMibDKCHWTable_Object = MibTable
raidExMibDKCHWTable = _RaidExMibDKCHWTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    raidExMibDKCHWTable.setStatus("mandatory")
_RaidExMibDKCHWEntry_Object = MibTableRow
raidExMibDKCHWEntry = _RaidExMibDKCHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1)
)
raidExMibDKCHWEntry.setIndexNames(
    (0, "HM800MIB", "dkcRaidListIndexSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKCHWEntry.setStatus("mandatory")
_DkcRaidListIndexSerialNumber_Type = Integer32
_DkcRaidListIndexSerialNumber_Object = MibTableColumn
dkcRaidListIndexSerialNumber = _DkcRaidListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 1),
    _DkcRaidListIndexSerialNumber_Type()
)
dkcRaidListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcRaidListIndexSerialNumber.setStatus("mandatory")


class _DkcHWProcessor_Type(Integer32):
    """Custom type dkcHWProcessor based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWProcessor_Type.__name__ = "Integer32"
_DkcHWProcessor_Object = MibTableColumn
dkcHWProcessor = _DkcHWProcessor_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 2),
    _DkcHWProcessor_Type()
)
dkcHWProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWProcessor.setStatus("mandatory")


class _DkcHWCSW_Type(Integer32):
    """Custom type dkcHWCSW based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWCSW_Type.__name__ = "Integer32"
_DkcHWCSW_Object = MibTableColumn
dkcHWCSW = _DkcHWCSW_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 3),
    _DkcHWCSW_Type()
)
dkcHWCSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWCSW.setStatus("mandatory")


class _DkcHWCache_Type(Integer32):
    """Custom type dkcHWCache based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWCache_Type.__name__ = "Integer32"
_DkcHWCache_Object = MibTableColumn
dkcHWCache = _DkcHWCache_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 4),
    _DkcHWCache_Type()
)
dkcHWCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWCache.setStatus("mandatory")


class _DkcHWSM_Type(Integer32):
    """Custom type dkcHWSM based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWSM_Type.__name__ = "Integer32"
_DkcHWSM_Object = MibTableColumn
dkcHWSM = _DkcHWSM_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 5),
    _DkcHWSM_Type()
)
dkcHWSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWSM.setStatus("mandatory")


class _DkcHWPS_Type(Integer32):
    """Custom type dkcHWPS based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWPS_Type.__name__ = "Integer32"
_DkcHWPS_Object = MibTableColumn
dkcHWPS = _DkcHWPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 6),
    _DkcHWPS_Type()
)
dkcHWPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWPS.setStatus("mandatory")


class _DkcHWBattery_Type(Integer32):
    """Custom type dkcHWBattery based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWBattery_Type.__name__ = "Integer32"
_DkcHWBattery_Object = MibTableColumn
dkcHWBattery = _DkcHWBattery_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 7),
    _DkcHWBattery_Type()
)
dkcHWBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWBattery.setStatus("mandatory")


class _DkcHWFan_Type(Integer32):
    """Custom type dkcHWFan based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWFan_Type.__name__ = "Integer32"
_DkcHWFan_Object = MibTableColumn
dkcHWFan = _DkcHWFan_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 8),
    _DkcHWFan_Type()
)
dkcHWFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWFan.setStatus("mandatory")


class _DkcHWEnvironment_Type(Integer32):
    """Custom type dkcHWEnvironment based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkcHWEnvironment_Type.__name__ = "Integer32"
_DkcHWEnvironment_Object = MibTableColumn
dkcHWEnvironment = _DkcHWEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 6, 1, 9),
    _DkcHWEnvironment_Type()
)
dkcHWEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkcHWEnvironment.setStatus("mandatory")
_RaidExMibDKUHWTable_Object = MibTable
raidExMibDKUHWTable = _RaidExMibDKUHWTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    raidExMibDKUHWTable.setStatus("mandatory")
_RaidExMibDKUHWEntry_Object = MibTableRow
raidExMibDKUHWEntry = _RaidExMibDKUHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1)
)
raidExMibDKUHWEntry.setIndexNames(
    (0, "HM800MIB", "dkuRaidListIndexSerialNumber"),
)
if mibBuilder.loadTexts:
    raidExMibDKUHWEntry.setStatus("mandatory")
_DkuRaidListIndexSerialNumber_Type = Integer32
_DkuRaidListIndexSerialNumber_Object = MibTableColumn
dkuRaidListIndexSerialNumber = _DkuRaidListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 1),
    _DkuRaidListIndexSerialNumber_Type()
)
dkuRaidListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuRaidListIndexSerialNumber.setStatus("mandatory")


class _DkuHWPS_Type(Integer32):
    """Custom type dkuHWPS based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkuHWPS_Type.__name__ = "Integer32"
_DkuHWPS_Object = MibTableColumn
dkuHWPS = _DkuHWPS_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 2),
    _DkuHWPS_Type()
)
dkuHWPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWPS.setStatus("mandatory")


class _DkuHWFan_Type(Integer32):
    """Custom type dkuHWFan based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkuHWFan_Type.__name__ = "Integer32"
_DkuHWFan_Object = MibTableColumn
dkuHWFan = _DkuHWFan_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 3),
    _DkuHWFan_Type()
)
dkuHWFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWFan.setStatus("mandatory")


class _DkuHWEnvironment_Type(Integer32):
    """Custom type dkuHWEnvironment based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkuHWEnvironment_Type.__name__ = "Integer32"
_DkuHWEnvironment_Object = MibTableColumn
dkuHWEnvironment = _DkuHWEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 4),
    _DkuHWEnvironment_Type()
)
dkuHWEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWEnvironment.setStatus("mandatory")


class _DkuHWDrive_Type(Integer32):
    """Custom type dkuHWDrive based on Integer32"""
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
        *(("noError", 1),
          ("acute", 2),
          ("serious", 3),
          ("moderate", 4),
          ("service", 5))
    )


_DkuHWDrive_Type.__name__ = "Integer32"
_DkuHWDrive_Object = MibTableColumn
dkuHWDrive = _DkuHWDrive_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 7, 1, 5),
    _DkuHWDrive_Type()
)
dkuHWDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dkuHWDrive.setStatus("mandatory")
_RaidExMibTrapListTable_Object = MibTable
raidExMibTrapListTable = _RaidExMibTrapListTable_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    raidExMibTrapListTable.setStatus("mandatory")
_RaidExMibTrapListEntry_Object = MibTableRow
raidExMibTrapListEntry = _RaidExMibTrapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1)
)
raidExMibTrapListEntry.setIndexNames(
    (0, "HM800MIB", "eventListIndexSerialNumber"),
    (0, "HM800MIB", "eventListIndexRecordNo"),
)
if mibBuilder.loadTexts:
    raidExMibTrapListEntry.setStatus("mandatory")
_EventListIndexSerialNumber_Type = Integer32
_EventListIndexSerialNumber_Object = MibTableColumn
eventListIndexSerialNumber = _EventListIndexSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 1),
    _EventListIndexSerialNumber_Type()
)
eventListIndexSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListIndexSerialNumber.setStatus("mandatory")


class _EventListNickname_Type(DisplayString):
    """Custom type eventListNickname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_EventListNickname_Type.__name__ = "DisplayString"
_EventListNickname_Object = MibTableColumn
eventListNickname = _EventListNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 2),
    _EventListNickname_Type()
)
eventListNickname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListNickname.setStatus("mandatory")
_EventListIndexRecordNo_Type = Counter32
_EventListIndexRecordNo_Object = MibTableColumn
eventListIndexRecordNo = _EventListIndexRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 3),
    _EventListIndexRecordNo_Type()
)
eventListIndexRecordNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListIndexRecordNo.setStatus("mandatory")


class _EventListREFCODE_Type(DisplayString):
    """Custom type eventListREFCODE based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_EventListREFCODE_Type.__name__ = "DisplayString"
_EventListREFCODE_Object = MibTableColumn
eventListREFCODE = _EventListREFCODE_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 4),
    _EventListREFCODE_Type()
)
eventListREFCODE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListREFCODE.setStatus("mandatory")


class _EventListDate_Type(DisplayString):
    """Custom type eventListDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_EventListDate_Type.__name__ = "DisplayString"
_EventListDate_Object = MibTableColumn
eventListDate = _EventListDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 5),
    _EventListDate_Type()
)
eventListDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListDate.setStatus("mandatory")


class _EventListTime_Type(DisplayString):
    """Custom type eventListTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EventListTime_Type.__name__ = "DisplayString"
_EventListTime_Object = MibTableColumn
eventListTime = _EventListTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 6),
    _EventListTime_Type()
)
eventListTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListTime.setStatus("mandatory")


class _EventListDescription_Type(DisplayString):
    """Custom type eventListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventListDescription_Type.__name__ = "DisplayString"
_EventListDescription_Object = MibTableColumn
eventListDescription = _EventListDescription_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 1, 1, 8, 1, 7),
    _EventListDescription_Type()
)
eventListDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventListDescription.setStatus("mandatory")
_RaidExMibDummyX_ObjectIdentity = ObjectIdentity
raidExMibDummyX = _RaidExMibDummyX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2)
)
_EventTrapSerialNumber_Type = Integer32
_EventTrapSerialNumber_Object = MibScalar
eventTrapSerialNumber = _EventTrapSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 1),
    _EventTrapSerialNumber_Type()
)
eventTrapSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapSerialNumber.setStatus("mandatory")
_EventTrapNickname_Type = DisplayString
_EventTrapNickname_Object = MibScalar
eventTrapNickname = _EventTrapNickname_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 2),
    _EventTrapNickname_Type()
)
eventTrapNickname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapNickname.setStatus("mandatory")
_EventTrapREFCODE_Type = DisplayString
_EventTrapREFCODE_Object = MibScalar
eventTrapREFCODE = _EventTrapREFCODE_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 3),
    _EventTrapREFCODE_Type()
)
eventTrapREFCODE.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapREFCODE.setStatus("mandatory")
_EventTrapPartsID_Type = ObjectIdentifier
_EventTrapPartsID_Object = MibScalar
eventTrapPartsID = _EventTrapPartsID_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 4),
    _EventTrapPartsID_Type()
)
eventTrapPartsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapPartsID.setStatus("mandatory")
_EventTrapDate_Type = DisplayString
_EventTrapDate_Object = MibScalar
eventTrapDate = _EventTrapDate_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 5),
    _EventTrapDate_Type()
)
eventTrapDate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapDate.setStatus("mandatory")
_EventTrapTime_Type = DisplayString
_EventTrapTime_Object = MibScalar
eventTrapTime = _EventTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 6),
    _EventTrapTime_Type()
)
eventTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapTime.setStatus("mandatory")


class _EventTrapDescription_Type(DisplayString):
    """Custom type eventTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventTrapDescription_Type.__name__ = "DisplayString"
_EventTrapDescription_Object = MibScalar
eventTrapDescription = _EventTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 116, 5, 11, 4, 2, 7),
    _EventTrapDescription_Type()
)
eventTrapDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTrapDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

raideventUseracute = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 1)
)
raideventUseracute.setObjects(
      *(("HM800MIB", "eventTrapSerialNumber"),
        ("HM800MIB", "eventTrapNickname"),
        ("HM800MIB", "eventTrapREFCODE"),
        ("HM800MIB", "eventTrapPartsID"),
        ("HM800MIB", "eventTrapDate"),
        ("HM800MIB", "eventTrapTime"),
        ("HM800MIB", "eventTrapDescription"))
)
if mibBuilder.loadTexts:
    raideventUseracute.setStatus(
        ""
    )

raideventUserserious = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 2)
)
raideventUserserious.setObjects(
      *(("HM800MIB", "eventTrapSerialNumber"),
        ("HM800MIB", "eventTrapNickname"),
        ("HM800MIB", "eventTrapREFCODE"),
        ("HM800MIB", "eventTrapPartsID"),
        ("HM800MIB", "eventTrapDate"),
        ("HM800MIB", "eventTrapTime"),
        ("HM800MIB", "eventTrapDescription"))
)
if mibBuilder.loadTexts:
    raideventUserserious.setStatus(
        ""
    )

raideventUsermoderate = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 3)
)
raideventUsermoderate.setObjects(
      *(("HM800MIB", "eventTrapSerialNumber"),
        ("HM800MIB", "eventTrapNickname"),
        ("HM800MIB", "eventTrapREFCODE"),
        ("HM800MIB", "eventTrapPartsID"),
        ("HM800MIB", "eventTrapDate"),
        ("HM800MIB", "eventTrapTime"),
        ("HM800MIB", "eventTrapDescription"))
)
if mibBuilder.loadTexts:
    raideventUsermoderate.setStatus(
        ""
    )

raideventUserservice = NotificationType(
    (1, 3, 6, 1, 4, 1, 116, 3, 11, 4, 1, 1, 0, 4)
)
raideventUserservice.setObjects(
      *(("HM800MIB", "eventTrapSerialNumber"),
        ("HM800MIB", "eventTrapNickname"),
        ("HM800MIB", "eventTrapREFCODE"),
        ("HM800MIB", "eventTrapPartsID"),
        ("HM800MIB", "eventTrapDate"),
        ("HM800MIB", "eventTrapTime"),
        ("HM800MIB", "eventTrapDescription"))
)
if mibBuilder.loadTexts:
    raideventUserservice.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM800MIB",
    **{"hitachi": hitachi,
       "system": system,
       "storage": storage,
       "raid": raid,
       "raidDummy": raidDummy,
       "raidRoot": raidRoot,
       "raideventUseracute": raideventUseracute,
       "raideventUserserious": raideventUserserious,
       "raideventUsermoderate": raideventUsermoderate,
       "raideventUserservice": raideventUserservice,
       "systemExMib": systemExMib,
       "storageExMib": storageExMib,
       "raidExMib": raidExMib,
       "raidExMibDummy": raidExMibDummy,
       "raidExMibRoot": raidExMibRoot,
       "raidExMibName": raidExMibName,
       "raidExMibVersion": raidExMibVersion,
       "raidExMibAgentVersion": raidExMibAgentVersion,
       "raidExMibDkcCount": raidExMibDkcCount,
       "raidExMibRaidListTable": raidExMibRaidListTable,
       "raidExMibRaidListEntry": raidExMibRaidListEntry,
       "raidlistSerialNumber": raidlistSerialNumber,
       "raidlistMibNickName": raidlistMibNickName,
       "raidlistDKCMainVersion": raidlistDKCMainVersion,
       "raidlistDKCProductName": raidlistDKCProductName,
       "raidExMibDKCHWTable": raidExMibDKCHWTable,
       "raidExMibDKCHWEntry": raidExMibDKCHWEntry,
       "dkcRaidListIndexSerialNumber": dkcRaidListIndexSerialNumber,
       "dkcHWProcessor": dkcHWProcessor,
       "dkcHWCSW": dkcHWCSW,
       "dkcHWCache": dkcHWCache,
       "dkcHWSM": dkcHWSM,
       "dkcHWPS": dkcHWPS,
       "dkcHWBattery": dkcHWBattery,
       "dkcHWFan": dkcHWFan,
       "dkcHWEnvironment": dkcHWEnvironment,
       "raidExMibDKUHWTable": raidExMibDKUHWTable,
       "raidExMibDKUHWEntry": raidExMibDKUHWEntry,
       "dkuRaidListIndexSerialNumber": dkuRaidListIndexSerialNumber,
       "dkuHWPS": dkuHWPS,
       "dkuHWFan": dkuHWFan,
       "dkuHWEnvironment": dkuHWEnvironment,
       "dkuHWDrive": dkuHWDrive,
       "raidExMibTrapListTable": raidExMibTrapListTable,
       "raidExMibTrapListEntry": raidExMibTrapListEntry,
       "eventListIndexSerialNumber": eventListIndexSerialNumber,
       "eventListNickname": eventListNickname,
       "eventListIndexRecordNo": eventListIndexRecordNo,
       "eventListREFCODE": eventListREFCODE,
       "eventListDate": eventListDate,
       "eventListTime": eventListTime,
       "eventListDescription": eventListDescription,
       "raidExMibDummyX": raidExMibDummyX,
       "eventTrapSerialNumber": eventTrapSerialNumber,
       "eventTrapNickname": eventTrapNickname,
       "eventTrapREFCODE": eventTrapREFCODE,
       "eventTrapPartsID": eventTrapPartsID,
       "eventTrapDate": eventTrapDate,
       "eventTrapTime": eventTrapTime,
       "eventTrapDescription": eventTrapDescription}
)
