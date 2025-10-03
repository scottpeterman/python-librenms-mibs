# SNMP MIB module (PACKETLOGIC-RAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-RAID-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:23 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hw,) = mibBuilder.importSymbols(
    "PACKETLOGIC-HW-MIB",
    "hw")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

raid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1)
)
if mibBuilder.loadTexts:
    raid.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaidCfg_ObjectIdentity = ObjectIdentity
raidCfg = _RaidCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1)
)
_AdpNumber_Type = Unsigned32
_AdpNumber_Object = MibScalar
adpNumber = _AdpNumber_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 1),
    _AdpNumber_Type()
)
adpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpNumber.setStatus("current")
_LdNumber_Type = Unsigned32
_LdNumber_Object = MibScalar
ldNumber = _LdNumber_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 2),
    _LdNumber_Type()
)
ldNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldNumber.setStatus("current")
_DiskNumber_Type = Unsigned32
_DiskNumber_Object = MibScalar
diskNumber = _DiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 1, 3),
    _DiskNumber_Type()
)
diskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskNumber.setStatus("current")
_Ld_Object = MibTable
ld = _Ld_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3)
)
if mibBuilder.loadTexts:
    ld.setStatus("current")
_LdEntry_Object = MibTableRow
ldEntry = _LdEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1)
)
ldEntry.setIndexNames(
    (0, "PACKETLOGIC-RAID-MIB", "ldEntryIndex"),
)
if mibBuilder.loadTexts:
    ldEntry.setStatus("current")
_LdId_Type = DisplayString
_LdId_Object = MibTableColumn
ldId = _LdId_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 1),
    _LdId_Type()
)
ldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldId.setStatus("current")
_LdState_Type = DisplayString
_LdState_Object = MibTableColumn
ldState = _LdState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 2),
    _LdState_Type()
)
ldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldState.setStatus("current")


class _LdEntryIndex_Type(Integer32):
    """Custom type ldEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LdEntryIndex_Type.__name__ = "Integer32"
_LdEntryIndex_Object = MibTableColumn
ldEntryIndex = _LdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 3, 1, 999),
    _LdEntryIndex_Type()
)
ldEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ldEntryIndex.setStatus("current")
_Disk_Object = MibTable
disk = _Disk_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4)
)
if mibBuilder.loadTexts:
    disk.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1)
)
diskEntry.setIndexNames(
    (0, "PACKETLOGIC-RAID-MIB", "diskEntryIndex"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")
_DiskId_Type = DisplayString
_DiskId_Object = MibTableColumn
diskId = _DiskId_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 1),
    _DiskId_Type()
)
diskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskId.setStatus("current")
_DiskState_Type = DisplayString
_DiskState_Object = MibTableColumn
diskState = _DiskState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 2),
    _DiskState_Type()
)
diskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskState.setStatus("current")
_DiskLabel_Type = DisplayString
_DiskLabel_Object = MibTableColumn
diskLabel = _DiskLabel_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 3),
    _DiskLabel_Type()
)
diskLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLabel.setStatus("current")


class _DiskEntryIndex_Type(Integer32):
    """Custom type diskEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DiskEntryIndex_Type.__name__ = "Integer32"
_DiskEntryIndex_Object = MibTableColumn
diskEntryIndex = _DiskEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 30, 1, 4, 1, 999),
    _DiskEntryIndex_Type()
)
diskEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskEntryIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-RAID-MIB",
    **{"raid": raid,
       "raidCfg": raidCfg,
       "adpNumber": adpNumber,
       "ldNumber": ldNumber,
       "diskNumber": diskNumber,
       "ld": ld,
       "ldEntry": ldEntry,
       "ldId": ldId,
       "ldState": ldState,
       "ldEntryIndex": ldEntryIndex,
       "disk": disk,
       "diskEntry": diskEntry,
       "diskId": diskId,
       "diskState": diskState,
       "diskLabel": diskLabel,
       "diskEntryIndex": diskEntryIndex}
)
