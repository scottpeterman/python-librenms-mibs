# SNMP MIB module (ALPINE-GEN-CARD-TDCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpineoe\ALPINE-GEN-CARD-TDCM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:46 2025
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

(alpineGeneric,) = mibBuilder.importSymbols(
    "ALPINE-ROOT",
    "alpineGeneric")

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

_AlpineGenCardTdcm_ObjectIdentity = ObjectIdentity
alpineGenCardTdcm = _AlpineGenCardTdcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2)
)
_AlpineGenCardTdcmInfosTable_Object = MibTable
alpineGenCardTdcmInfosTable = _AlpineGenCardTdcmInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alpineGenCardTdcmInfosTable.setStatus("current")
_AlpineGenCardTdcmInfosEntry_Object = MibTableRow
alpineGenCardTdcmInfosEntry = _AlpineGenCardTdcmInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1)
)
alpineGenCardTdcmInfosEntry.setIndexNames(
    (0, "ALPINE-GEN-CARD-TDCM-MIB", "gctiSlotNum"),
)
if mibBuilder.loadTexts:
    alpineGenCardTdcmInfosEntry.setStatus("current")


class _GctiSlotNum_Type(Integer32):
    """Custom type gctiSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GctiSlotNum_Type.__name__ = "Integer32"
_GctiSlotNum_Object = MibTableColumn
gctiSlotNum = _GctiSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 1),
    _GctiSlotNum_Type()
)
gctiSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gctiSlotNum.setStatus("current")


class _GctiWorkMode_Type(Integer32):
    """Custom type gctiWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GctiWorkMode_Type.__name__ = "Integer32"
_GctiWorkMode_Object = MibTableColumn
gctiWorkMode = _GctiWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 2),
    _GctiWorkMode_Type()
)
gctiWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gctiWorkMode.setStatus("current")
_GctiDefaultDispersion_Type = Integer32
_GctiDefaultDispersion_Object = MibTableColumn
gctiDefaultDispersion = _GctiDefaultDispersion_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 3),
    _GctiDefaultDispersion_Type()
)
gctiDefaultDispersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gctiDefaultDispersion.setStatus("current")
if mibBuilder.loadTexts:
    gctiDefaultDispersion.setUnits("ps/nm*km")
_GctiCurrentDispersion_Type = Integer32
_GctiCurrentDispersion_Object = MibTableColumn
gctiCurrentDispersion = _GctiCurrentDispersion_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 4),
    _GctiCurrentDispersion_Type()
)
gctiCurrentDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gctiCurrentDispersion.setStatus("current")
if mibBuilder.loadTexts:
    gctiCurrentDispersion.setUnits("ps/nm*km")


class _GctiAutoModeSwitch_Type(Integer32):
    """Custom type gctiAutoModeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GctiAutoModeSwitch_Type.__name__ = "Integer32"
_GctiAutoModeSwitch_Object = MibTableColumn
gctiAutoModeSwitch = _GctiAutoModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 5),
    _GctiAutoModeSwitch_Type()
)
gctiAutoModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gctiAutoModeSwitch.setStatus("current")


class _GctiSaveConfig_Type(Integer32):
    """Custom type gctiSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GctiSaveConfig_Type.__name__ = "Integer32"
_GctiSaveConfig_Object = MibTableColumn
gctiSaveConfig = _GctiSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 52326, 1, 2, 1, 1, 6),
    _GctiSaveConfig_Type()
)
gctiSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gctiSaveConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPINE-GEN-CARD-TDCM-MIB",
    **{"alpineGenCardTdcm": alpineGenCardTdcm,
       "alpineGenCardTdcmInfosTable": alpineGenCardTdcmInfosTable,
       "alpineGenCardTdcmInfosEntry": alpineGenCardTdcmInfosEntry,
       "gctiSlotNum": gctiSlotNum,
       "gctiWorkMode": gctiWorkMode,
       "gctiDefaultDispersion": gctiDefaultDispersion,
       "gctiCurrentDispersion": gctiCurrentDispersion,
       "gctiAutoModeSwitch": gctiAutoModeSwitch,
       "gctiSaveConfig": gctiSaveConfig}
)
