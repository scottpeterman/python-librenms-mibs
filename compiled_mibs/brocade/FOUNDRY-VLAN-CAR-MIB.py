# SNMP MIB module (FOUNDRY-VLAN-CAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\brocade\FOUNDRY-VLAN-CAR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:31 2025
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

(PacketSource,
 RateLimitAction,
 RateLimitType) = mibBuilder.importSymbols(
    "FOUNDRY-CAR-MIB",
    "PacketSource",
    "RateLimitAction",
    "RateLimitType")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

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

snVLanCAR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17)
)
if mibBuilder.loadTexts:
    snVLanCAR.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnVLanCARs_ObjectIdentity = ObjectIdentity
snVLanCARs = _SnVLanCARs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1)
)
_SnVLanCARTable_Object = MibTable
snVLanCARTable = _SnVLanCARTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1)
)
if mibBuilder.loadTexts:
    snVLanCARTable.setStatus("current")
_SnVLanCAREntry_Object = MibTableRow
snVLanCAREntry = _SnVLanCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1)
)
snVLanCAREntry.setIndexNames(
    (0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARVLanId"),
    (0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARDirection"),
    (0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARRowIndex"),
)
if mibBuilder.loadTexts:
    snVLanCAREntry.setStatus("current")


class _SnVLanCARVLanId_Type(Integer32):
    """Custom type snVLanCARVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnVLanCARVLanId_Type.__name__ = "Integer32"
_SnVLanCARVLanId_Object = MibTableColumn
snVLanCARVLanId = _SnVLanCARVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 1),
    _SnVLanCARVLanId_Type()
)
snVLanCARVLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARVLanId.setStatus("current")
_SnVLanCARDirection_Type = PacketSource
_SnVLanCARDirection_Object = MibTableColumn
snVLanCARDirection = _SnVLanCARDirection_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 2),
    _SnVLanCARDirection_Type()
)
snVLanCARDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARDirection.setStatus("current")


class _SnVLanCARRowIndex_Type(Integer32):
    """Custom type snVLanCARRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnVLanCARRowIndex_Type.__name__ = "Integer32"
_SnVLanCARRowIndex_Object = MibTableColumn
snVLanCARRowIndex = _SnVLanCARRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 3),
    _SnVLanCARRowIndex_Type()
)
snVLanCARRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARRowIndex.setStatus("current")
_SnVLanCARType_Type = RateLimitType
_SnVLanCARType_Object = MibTableColumn
snVLanCARType = _SnVLanCARType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 4),
    _SnVLanCARType_Type()
)
snVLanCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARType.setStatus("current")
_SnVLanCARAccIdx_Type = Integer32
_SnVLanCARAccIdx_Object = MibTableColumn
snVLanCARAccIdx = _SnVLanCARAccIdx_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 5),
    _SnVLanCARAccIdx_Type()
)
snVLanCARAccIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARAccIdx.setStatus("current")
_SnVLanCARRate_Type = Integer32
_SnVLanCARRate_Object = MibTableColumn
snVLanCARRate = _SnVLanCARRate_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 6),
    _SnVLanCARRate_Type()
)
snVLanCARRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARRate.setStatus("current")
_SnVLanCARLimit_Type = Integer32
_SnVLanCARLimit_Object = MibTableColumn
snVLanCARLimit = _SnVLanCARLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 7),
    _SnVLanCARLimit_Type()
)
snVLanCARLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARLimit.setStatus("current")
_SnVLanCARExtLimit_Type = Integer32
_SnVLanCARExtLimit_Object = MibTableColumn
snVLanCARExtLimit = _SnVLanCARExtLimit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 8),
    _SnVLanCARExtLimit_Type()
)
snVLanCARExtLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARExtLimit.setStatus("current")
_SnVLanCARConformAction_Type = RateLimitAction
_SnVLanCARConformAction_Object = MibTableColumn
snVLanCARConformAction = _SnVLanCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 9),
    _SnVLanCARConformAction_Type()
)
snVLanCARConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARConformAction.setStatus("current")
_SnVLanCARExceedAction_Type = RateLimitAction
_SnVLanCARExceedAction_Object = MibTableColumn
snVLanCARExceedAction = _SnVLanCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 10),
    _SnVLanCARExceedAction_Type()
)
snVLanCARExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARExceedAction.setStatus("current")
_SnVLanCARStatSwitchedPkts_Type = Counter64
_SnVLanCARStatSwitchedPkts_Object = MibTableColumn
snVLanCARStatSwitchedPkts = _SnVLanCARStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 11),
    _SnVLanCARStatSwitchedPkts_Type()
)
snVLanCARStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARStatSwitchedPkts.setStatus("current")
_SnVLanCARStatSwitchedBytes_Type = Counter64
_SnVLanCARStatSwitchedBytes_Object = MibTableColumn
snVLanCARStatSwitchedBytes = _SnVLanCARStatSwitchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 12),
    _SnVLanCARStatSwitchedBytes_Type()
)
snVLanCARStatSwitchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARStatSwitchedBytes.setStatus("current")
_SnVLanCARStatFilteredPkts_Type = Counter64
_SnVLanCARStatFilteredPkts_Object = MibTableColumn
snVLanCARStatFilteredPkts = _SnVLanCARStatFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 13),
    _SnVLanCARStatFilteredPkts_Type()
)
snVLanCARStatFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARStatFilteredPkts.setStatus("current")
_SnVLanCARStatFilteredBytes_Type = Counter64
_SnVLanCARStatFilteredBytes_Object = MibTableColumn
snVLanCARStatFilteredBytes = _SnVLanCARStatFilteredBytes_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 14),
    _SnVLanCARStatFilteredBytes_Type()
)
snVLanCARStatFilteredBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARStatFilteredBytes.setStatus("current")
_SnVLanCARStatCurBurst_Type = Gauge32
_SnVLanCARStatCurBurst_Object = MibTableColumn
snVLanCARStatCurBurst = _SnVLanCARStatCurBurst_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 15),
    _SnVLanCARStatCurBurst_Type()
)
snVLanCARStatCurBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snVLanCARStatCurBurst.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-VLAN-CAR-MIB",
    **{"snVLanCAR": snVLanCAR,
       "snVLanCARs": snVLanCARs,
       "snVLanCARTable": snVLanCARTable,
       "snVLanCAREntry": snVLanCAREntry,
       "snVLanCARVLanId": snVLanCARVLanId,
       "snVLanCARDirection": snVLanCARDirection,
       "snVLanCARRowIndex": snVLanCARRowIndex,
       "snVLanCARType": snVLanCARType,
       "snVLanCARAccIdx": snVLanCARAccIdx,
       "snVLanCARRate": snVLanCARRate,
       "snVLanCARLimit": snVLanCARLimit,
       "snVLanCARExtLimit": snVLanCARExtLimit,
       "snVLanCARConformAction": snVLanCARConformAction,
       "snVLanCARExceedAction": snVLanCARExceedAction,
       "snVLanCARStatSwitchedPkts": snVLanCARStatSwitchedPkts,
       "snVLanCARStatSwitchedBytes": snVLanCARStatSwitchedBytes,
       "snVLanCARStatFilteredPkts": snVLanCARStatFilteredPkts,
       "snVLanCARStatFilteredBytes": snVLanCARStatFilteredBytes,
       "snVLanCARStatCurBurst": snVLanCARStatCurBurst}
)
