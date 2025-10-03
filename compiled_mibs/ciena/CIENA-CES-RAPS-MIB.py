# SNMP MIB module (CIENA-CES-RAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-RAPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:51 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesRapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20)
)
if mibBuilder.loadTexts:
    cienaCesRapsMIB.setRevisions(
        ("2017-06-07 00:00",
         "2017-01-23 00:00",
         "2014-07-04 00:00",
         "2011-04-16 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesRapsMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBObjects = _CienaCesRapsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1)
)
_CienaCesRapsGlobal_ObjectIdentity = ObjectIdentity
cienaCesRapsGlobal = _CienaCesRapsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1)
)
_CienaCesRapsGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCesRapsGlobalAttrs = _CienaCesRapsGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1, 1)
)


class _CienaCesRapsState_Type(CienaGlobalState):
    """Custom type cienaCesRapsState based on CienaGlobalState"""
    defaultValue = 1


_CienaCesRapsState_Type.__name__ = "CienaGlobalState"
_CienaCesRapsState_Object = MibScalar
cienaCesRapsState = _CienaCesRapsState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1, 1, 1),
    _CienaCesRapsState_Type()
)
cienaCesRapsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsState.setStatus("current")
_CienaCesRapsNodeId_Type = MacAddress
_CienaCesRapsNodeId_Object = MibScalar
cienaCesRapsNodeId = _CienaCesRapsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1, 1, 2),
    _CienaCesRapsNodeId_Type()
)
cienaCesRapsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsNodeId.setStatus("current")


class _CienaCesRapsEtherType_Type(OctetString):
    """Custom type cienaCesRapsEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_CienaCesRapsEtherType_Type.__name__ = "OctetString"
_CienaCesRapsEtherType_Object = MibScalar
cienaCesRapsEtherType = _CienaCesRapsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1, 1, 3),
    _CienaCesRapsEtherType_Type()
)
cienaCesRapsEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsEtherType.setStatus("current")
_CienaCesRapsNumberOfRings_Type = Integer32
_CienaCesRapsNumberOfRings_Object = MibScalar
cienaCesRapsNumberOfRings = _CienaCesRapsNumberOfRings_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 1, 1, 4),
    _CienaCesRapsNumberOfRings_Type()
)
cienaCesRapsNumberOfRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsNumberOfRings.setStatus("current")
_CienaCesRapsLogicalRing_ObjectIdentity = ObjectIdentity
cienaCesRapsLogicalRing = _CienaCesRapsLogicalRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2)
)
_CienaCesRapsLogicalRingTable_Object = MibTable
cienaCesRapsLogicalRingTable = _CienaCesRapsLogicalRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingTable.setStatus("current")
_CienaCesRapsLogicalRingEntry_Object = MibTableRow
cienaCesRapsLogicalRingEntry = _CienaCesRapsLogicalRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1)
)
cienaCesRapsLogicalRingEntry.setIndexNames(
    (0, "CIENA-CES-RAPS-MIB", "cienaCesRapsLogicalRingIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEntry.setStatus("current")


class _CienaCesRapsLogicalRingIndex_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CienaCesRapsLogicalRingIndex_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingIndex_Object = MibTableColumn
cienaCesRapsLogicalRingIndex = _CienaCesRapsLogicalRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 1),
    _CienaCesRapsLogicalRingIndex_Type()
)
cienaCesRapsLogicalRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingIndex.setStatus("current")


class _CienaCesRapsLogicalRingName_Type(DisplayString):
    """Custom type cienaCesRapsLogicalRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesRapsLogicalRingName_Type.__name__ = "DisplayString"
_CienaCesRapsLogicalRingName_Object = MibTableColumn
cienaCesRapsLogicalRingName = _CienaCesRapsLogicalRingName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 2),
    _CienaCesRapsLogicalRingName_Type()
)
cienaCesRapsLogicalRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingName.setStatus("current")


class _CienaCesRapsLogicalRingId_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesRapsLogicalRingId_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingId_Object = MibTableColumn
cienaCesRapsLogicalRingId = _CienaCesRapsLogicalRingId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 3),
    _CienaCesRapsLogicalRingId_Type()
)
cienaCesRapsLogicalRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingId.setStatus("current")


class _CienaCesRapsLogicalRingGuardTime_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingGuardTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_CienaCesRapsLogicalRingGuardTime_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingGuardTime_Object = MibTableColumn
cienaCesRapsLogicalRingGuardTime = _CienaCesRapsLogicalRingGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 4),
    _CienaCesRapsLogicalRingGuardTime_Type()
)
cienaCesRapsLogicalRingGuardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingGuardTime.setUnits("milliseconds")


class _CienaCesRapsLogicalRingWtr_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingWtr based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CienaCesRapsLogicalRingWtr_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingWtr_Object = MibTableColumn
cienaCesRapsLogicalRingWtr = _CienaCesRapsLogicalRingWtr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 5),
    _CienaCesRapsLogicalRingWtr_Type()
)
cienaCesRapsLogicalRingWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWtr.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWtr.setUnits("minutes")
_CienaCesRapsLogicalRingWtb_Type = Integer32
_CienaCesRapsLogicalRingWtb_Object = MibTableColumn
cienaCesRapsLogicalRingWtb = _CienaCesRapsLogicalRingWtb_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 6),
    _CienaCesRapsLogicalRingWtb_Type()
)
cienaCesRapsLogicalRingWtb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWtb.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWtb.setUnits("minutes")
_CienaCesRapsLogicalRingWestPortId_Type = Integer32
_CienaCesRapsLogicalRingWestPortId_Object = MibTableColumn
cienaCesRapsLogicalRingWestPortId = _CienaCesRapsLogicalRingWestPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 7),
    _CienaCesRapsLogicalRingWestPortId_Type()
)
cienaCesRapsLogicalRingWestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWestPortId.setStatus("current")


class _CienaCesRapsLogicalRingWestHoldOffTime_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingWestHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CienaCesRapsLogicalRingWestHoldOffTime_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingWestHoldOffTime_Object = MibTableColumn
cienaCesRapsLogicalRingWestHoldOffTime = _CienaCesRapsLogicalRingWestHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 8),
    _CienaCesRapsLogicalRingWestHoldOffTime_Type()
)
cienaCesRapsLogicalRingWestHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWestHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWestHoldOffTime.setUnits("milliseconds")


class _CienaCesRapsLogicalRingWestForce_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingWestForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsLogicalRingWestForce_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingWestForce_Object = MibTableColumn
cienaCesRapsLogicalRingWestForce = _CienaCesRapsLogicalRingWestForce_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 9),
    _CienaCesRapsLogicalRingWestForce_Type()
)
cienaCesRapsLogicalRingWestForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWestForce.setStatus("current")


class _CienaCesRapsLogicalRingWestCfmService_Type(DisplayString):
    """Custom type cienaCesRapsLogicalRingWestCfmService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesRapsLogicalRingWestCfmService_Type.__name__ = "DisplayString"
_CienaCesRapsLogicalRingWestCfmService_Object = MibTableColumn
cienaCesRapsLogicalRingWestCfmService = _CienaCesRapsLogicalRingWestCfmService_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 10),
    _CienaCesRapsLogicalRingWestCfmService_Type()
)
cienaCesRapsLogicalRingWestCfmService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingWestCfmService.setStatus("current")
_CienaCesRapsLogicalRingEastPortId_Type = Integer32
_CienaCesRapsLogicalRingEastPortId_Object = MibTableColumn
cienaCesRapsLogicalRingEastPortId = _CienaCesRapsLogicalRingEastPortId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 11),
    _CienaCesRapsLogicalRingEastPortId_Type()
)
cienaCesRapsLogicalRingEastPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEastPortId.setStatus("current")


class _CienaCesRapsLogicalRingEastHoldOffTime_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingEastHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CienaCesRapsLogicalRingEastHoldOffTime_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingEastHoldOffTime_Object = MibTableColumn
cienaCesRapsLogicalRingEastHoldOffTime = _CienaCesRapsLogicalRingEastHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 12),
    _CienaCesRapsLogicalRingEastHoldOffTime_Type()
)
cienaCesRapsLogicalRingEastHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEastHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEastHoldOffTime.setUnits("milliseconds")


class _CienaCesRapsLogicalRingEastForce_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingEastForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsLogicalRingEastForce_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingEastForce_Object = MibTableColumn
cienaCesRapsLogicalRingEastForce = _CienaCesRapsLogicalRingEastForce_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 13),
    _CienaCesRapsLogicalRingEastForce_Type()
)
cienaCesRapsLogicalRingEastForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEastForce.setStatus("current")


class _CienaCesRapsLogicalRingEastCfmService_Type(DisplayString):
    """Custom type cienaCesRapsLogicalRingEastCfmService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesRapsLogicalRingEastCfmService_Type.__name__ = "DisplayString"
_CienaCesRapsLogicalRingEastCfmService_Object = MibTableColumn
cienaCesRapsLogicalRingEastCfmService = _CienaCesRapsLogicalRingEastCfmService_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 14),
    _CienaCesRapsLogicalRingEastCfmService_Type()
)
cienaCesRapsLogicalRingEastCfmService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingEastCfmService.setStatus("current")


class _CienaCesRapsLogicalRingNumberOfVirtualRings_Type(Integer32):
    """Custom type cienaCesRapsLogicalRingNumberOfVirtualRings based on Integer32"""
    defaultValue = 0


_CienaCesRapsLogicalRingNumberOfVirtualRings_Type.__name__ = "Integer32"
_CienaCesRapsLogicalRingNumberOfVirtualRings_Object = MibTableColumn
cienaCesRapsLogicalRingNumberOfVirtualRings = _CienaCesRapsLogicalRingNumberOfVirtualRings_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 2, 1, 1, 15),
    _CienaCesRapsLogicalRingNumberOfVirtualRings_Type()
)
cienaCesRapsLogicalRingNumberOfVirtualRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsLogicalRingNumberOfVirtualRings.setStatus("current")
_CienaCesRapsVirtualRing_ObjectIdentity = ObjectIdentity
cienaCesRapsVirtualRing = _CienaCesRapsVirtualRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3)
)
_CienaCesRapsVirtualRingTable_Object = MibTable
cienaCesRapsVirtualRingTable = _CienaCesRapsVirtualRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingTable.setStatus("current")
_CienaCesRapsVirtualRingEntry_Object = MibTableRow
cienaCesRapsVirtualRingEntry = _CienaCesRapsVirtualRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1)
)
cienaCesRapsVirtualRingEntry.setIndexNames(
    (0, "CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingIndex"),
)
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEntry.setStatus("current")


class _CienaCesRapsVirtualRingIndex_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_CienaCesRapsVirtualRingIndex_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingIndex_Object = MibTableColumn
cienaCesRapsVirtualRingIndex = _CienaCesRapsVirtualRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 1),
    _CienaCesRapsVirtualRingIndex_Type()
)
cienaCesRapsVirtualRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingIndex.setStatus("current")


class _CienaCesRapsVirtualRingName_Type(DisplayString):
    """Custom type cienaCesRapsVirtualRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesRapsVirtualRingName_Type.__name__ = "DisplayString"
_CienaCesRapsVirtualRingName_Object = MibTableColumn
cienaCesRapsVirtualRingName = _CienaCesRapsVirtualRingName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 2),
    _CienaCesRapsVirtualRingName_Type()
)
cienaCesRapsVirtualRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingName.setStatus("current")


class _CienaCesRapsVirtualRingVid_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CienaCesRapsVirtualRingVid_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingVid_Object = MibTableColumn
cienaCesRapsVirtualRingVid = _CienaCesRapsVirtualRingVid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 3),
    _CienaCesRapsVirtualRingVid_Type()
)
cienaCesRapsVirtualRingVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingVid.setStatus("current")


class _CienaCesRapsVirtualRingLogicalRingId_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingLogicalRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CienaCesRapsVirtualRingLogicalRingId_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingLogicalRingId_Object = MibTableColumn
cienaCesRapsVirtualRingLogicalRingId = _CienaCesRapsVirtualRingLogicalRingId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 4),
    _CienaCesRapsVirtualRingLogicalRingId_Type()
)
cienaCesRapsVirtualRingLogicalRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingLogicalRingId.setStatus("current")


class _CienaCesRapsVirtualRingMel_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingMel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesRapsVirtualRingMel_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingMel_Object = MibTableColumn
cienaCesRapsVirtualRingMel = _CienaCesRapsVirtualRingMel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 5),
    _CienaCesRapsVirtualRingMel_Type()
)
cienaCesRapsVirtualRingMel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingMel.setStatus("current")


class _CienaCesRapsVirtualRingRevertive_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingRevertive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsVirtualRingRevertive_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingRevertive_Object = MibTableColumn
cienaCesRapsVirtualRingRevertive = _CienaCesRapsVirtualRingRevertive_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 6),
    _CienaCesRapsVirtualRingRevertive_Type()
)
cienaCesRapsVirtualRingRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingRevertive.setStatus("current")


class _CienaCesRapsVirtualRingState_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingState based on Integer32"""
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
        *(("adminDisabled", 1),
          ("ok", 2),
          ("protecting", 3),
          ("recovering", 4),
          ("init", 5),
          ("none", 6))
    )


_CienaCesRapsVirtualRingState_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingState_Object = MibTableColumn
cienaCesRapsVirtualRingState = _CienaCesRapsVirtualRingState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 7),
    _CienaCesRapsVirtualRingState_Type()
)
cienaCesRapsVirtualRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingState.setStatus("current")


class _CienaCesRapsVirtualRingStatus_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("localSignalFail", 2),
          ("localForceSwitch", 3),
          ("remoteOrOtherPortSignalFail", 4),
          ("remoteOrOtherPortForceSwitch", 5),
          ("provisioningMismatch", 6),
          ("noRapsPduReceived", 7),
          ("noRplOwnerDetected", 8))
    )


_CienaCesRapsVirtualRingStatus_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingStatus_Object = MibTableColumn
cienaCesRapsVirtualRingStatus = _CienaCesRapsVirtualRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 8),
    _CienaCesRapsVirtualRingStatus_Type()
)
cienaCesRapsVirtualRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingStatus.setStatus("current")


class _CienaCesRapsVirtualRingAlarm_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingAlarm based on Integer32"""
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
        *(("clear", 1),
          ("protectionSwitching", 2),
          ("provisionMismatch", 3),
          ("noRapsPduReceived", 4),
          ("noRplOwnerDetected", 5))
    )


_CienaCesRapsVirtualRingAlarm_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingAlarm_Object = MibTableColumn
cienaCesRapsVirtualRingAlarm = _CienaCesRapsVirtualRingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 9),
    _CienaCesRapsVirtualRingAlarm_Type()
)
cienaCesRapsVirtualRingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingAlarm.setStatus("current")
_CienaCesRapsVirtualRingNumOfSwitchOvers_Type = Integer32
_CienaCesRapsVirtualRingNumOfSwitchOvers_Object = MibTableColumn
cienaCesRapsVirtualRingNumOfSwitchOvers = _CienaCesRapsVirtualRingNumOfSwitchOvers_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 10),
    _CienaCesRapsVirtualRingNumOfSwitchOvers_Type()
)
cienaCesRapsVirtualRingNumOfSwitchOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingNumOfSwitchOvers.setStatus("current")
_CienaCesRapsVirtualRingUptimeFromLastFailure_Type = Integer32
_CienaCesRapsVirtualRingUptimeFromLastFailure_Object = MibTableColumn
cienaCesRapsVirtualRingUptimeFromLastFailure = _CienaCesRapsVirtualRingUptimeFromLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 11),
    _CienaCesRapsVirtualRingUptimeFromLastFailure_Type()
)
cienaCesRapsVirtualRingUptimeFromLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingUptimeFromLastFailure.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingUptimeFromLastFailure.setUnits("seconds")
_CienaCesRapsVirtualRingTotalDownTime_Type = Integer32
_CienaCesRapsVirtualRingTotalDownTime_Object = MibTableColumn
cienaCesRapsVirtualRingTotalDownTime = _CienaCesRapsVirtualRingTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 12),
    _CienaCesRapsVirtualRingTotalDownTime_Type()
)
cienaCesRapsVirtualRingTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingTotalDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingTotalDownTime.setUnits("seconds")


class _CienaCesRapsVirtualRingWestPortRpl_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingWestPortRpl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2))
    )


_CienaCesRapsVirtualRingWestPortRpl_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingWestPortRpl_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortRpl = _CienaCesRapsVirtualRingWestPortRpl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 13),
    _CienaCesRapsVirtualRingWestPortRpl_Type()
)
cienaCesRapsVirtualRingWestPortRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortRpl.setStatus("current")


class _CienaCesRapsVirtualRingWestPortState_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingWestPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("forwarding", 2),
          ("blocked", 3))
    )


_CienaCesRapsVirtualRingWestPortState_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingWestPortState_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortState = _CienaCesRapsVirtualRingWestPortState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 14),
    _CienaCesRapsVirtualRingWestPortState_Type()
)
cienaCesRapsVirtualRingWestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortState.setStatus("current")


class _CienaCesRapsVirtualRingWestPortStatus_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingWestPortStatus based on Integer32"""
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
        *(("oK", 1),
          ("down", 2),
          ("ccmFailure", 3),
          ("localForceSwitch", 4),
          ("remoteForceSwitch", 5),
          ("remoteSignalFailure", 6))
    )


_CienaCesRapsVirtualRingWestPortStatus_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingWestPortStatus_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortStatus = _CienaCesRapsVirtualRingWestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 15),
    _CienaCesRapsVirtualRingWestPortStatus_Type()
)
cienaCesRapsVirtualRingWestPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortStatus.setStatus("current")
_CienaCesRapsVirtualRingWestPortNrRxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortNrRxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortNrRxd = _CienaCesRapsVirtualRingWestPortNrRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 16),
    _CienaCesRapsVirtualRingWestPortNrRxd_Type()
)
cienaCesRapsVirtualRingWestPortNrRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortNrRxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortNrTxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortNrTxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortNrTxd = _CienaCesRapsVirtualRingWestPortNrTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 17),
    _CienaCesRapsVirtualRingWestPortNrTxd_Type()
)
cienaCesRapsVirtualRingWestPortNrTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortNrTxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortSfRxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortSfRxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortSfRxd = _CienaCesRapsVirtualRingWestPortSfRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 18),
    _CienaCesRapsVirtualRingWestPortSfRxd_Type()
)
cienaCesRapsVirtualRingWestPortSfRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortSfRxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortSfTxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortSfTxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortSfTxd = _CienaCesRapsVirtualRingWestPortSfTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 19),
    _CienaCesRapsVirtualRingWestPortSfTxd_Type()
)
cienaCesRapsVirtualRingWestPortSfTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortSfTxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortFsRxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortFsRxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortFsRxd = _CienaCesRapsVirtualRingWestPortFsRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 20),
    _CienaCesRapsVirtualRingWestPortFsRxd_Type()
)
cienaCesRapsVirtualRingWestPortFsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortFsRxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortFsTxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortFsTxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortFsTxd = _CienaCesRapsVirtualRingWestPortFsTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 21),
    _CienaCesRapsVirtualRingWestPortFsTxd_Type()
)
cienaCesRapsVirtualRingWestPortFsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortFsTxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortNrRbRxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortNrRbRxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortNrRbRxd = _CienaCesRapsVirtualRingWestPortNrRbRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 22),
    _CienaCesRapsVirtualRingWestPortNrRbRxd_Type()
)
cienaCesRapsVirtualRingWestPortNrRbRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortNrRbRxd.setStatus("current")
_CienaCesRapsVirtualRingWestPortNrRbTxd_Type = Integer32
_CienaCesRapsVirtualRingWestPortNrRbTxd_Object = MibTableColumn
cienaCesRapsVirtualRingWestPortNrRbTxd = _CienaCesRapsVirtualRingWestPortNrRbTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 23),
    _CienaCesRapsVirtualRingWestPortNrRbTxd_Type()
)
cienaCesRapsVirtualRingWestPortNrRbTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestPortNrRbTxd.setStatus("current")


class _CienaCesRapsVirtualRingEastPortRpl_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingEastPortRpl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2))
    )


_CienaCesRapsVirtualRingEastPortRpl_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingEastPortRpl_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortRpl = _CienaCesRapsVirtualRingEastPortRpl_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 24),
    _CienaCesRapsVirtualRingEastPortRpl_Type()
)
cienaCesRapsVirtualRingEastPortRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortRpl.setStatus("current")


class _CienaCesRapsVirtualRingEastPortState_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingEastPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("forwarding", 2),
          ("blocked", 3))
    )


_CienaCesRapsVirtualRingEastPortState_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingEastPortState_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortState = _CienaCesRapsVirtualRingEastPortState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 25),
    _CienaCesRapsVirtualRingEastPortState_Type()
)
cienaCesRapsVirtualRingEastPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortState.setStatus("current")


class _CienaCesRapsVirtualRingEastPortStatus_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingEastPortStatus based on Integer32"""
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
        *(("ok", 1),
          ("down", 2),
          ("ccmFailure", 3),
          ("localForceSwitch", 4),
          ("remoteForceSwitch", 5),
          ("remoteSignalFailure", 6))
    )


_CienaCesRapsVirtualRingEastPortStatus_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingEastPortStatus_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortStatus = _CienaCesRapsVirtualRingEastPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 26),
    _CienaCesRapsVirtualRingEastPortStatus_Type()
)
cienaCesRapsVirtualRingEastPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortStatus.setStatus("current")
_CienaCesRapsVirtualRingEastPortNrRxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortNrRxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortNrRxd = _CienaCesRapsVirtualRingEastPortNrRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 27),
    _CienaCesRapsVirtualRingEastPortNrRxd_Type()
)
cienaCesRapsVirtualRingEastPortNrRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortNrRxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortNrTxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortNrTxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortNrTxd = _CienaCesRapsVirtualRingEastPortNrTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 28),
    _CienaCesRapsVirtualRingEastPortNrTxd_Type()
)
cienaCesRapsVirtualRingEastPortNrTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortNrTxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortSfRxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortSfRxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortSfRxd = _CienaCesRapsVirtualRingEastPortSfRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 29),
    _CienaCesRapsVirtualRingEastPortSfRxd_Type()
)
cienaCesRapsVirtualRingEastPortSfRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortSfRxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortSfTxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortSfTxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortSfTxd = _CienaCesRapsVirtualRingEastPortSfTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 30),
    _CienaCesRapsVirtualRingEastPortSfTxd_Type()
)
cienaCesRapsVirtualRingEastPortSfTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortSfTxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortFsRxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortFsRxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortFsRxd = _CienaCesRapsVirtualRingEastPortFsRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 31),
    _CienaCesRapsVirtualRingEastPortFsRxd_Type()
)
cienaCesRapsVirtualRingEastPortFsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortFsRxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortFsTxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortFsTxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortFsTxd = _CienaCesRapsVirtualRingEastPortFsTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 32),
    _CienaCesRapsVirtualRingEastPortFsTxd_Type()
)
cienaCesRapsVirtualRingEastPortFsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortFsTxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortNrRbRxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortNrRbRxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortNrRbRxd = _CienaCesRapsVirtualRingEastPortNrRbRxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 33),
    _CienaCesRapsVirtualRingEastPortNrRbRxd_Type()
)
cienaCesRapsVirtualRingEastPortNrRbRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortNrRbRxd.setStatus("current")
_CienaCesRapsVirtualRingEastPortNrRbTxd_Type = Integer32
_CienaCesRapsVirtualRingEastPortNrRbTxd_Object = MibTableColumn
cienaCesRapsVirtualRingEastPortNrRbTxd = _CienaCesRapsVirtualRingEastPortNrRbTxd_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 34),
    _CienaCesRapsVirtualRingEastPortNrRbTxd_Type()
)
cienaCesRapsVirtualRingEastPortNrRbTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastPortNrRbTxd.setStatus("current")


class _CienaCesRapsVirtualRingType_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2))
    )


_CienaCesRapsVirtualRingType_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingType_Object = MibTableColumn
cienaCesRapsVirtualRingType = _CienaCesRapsVirtualRingType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 35),
    _CienaCesRapsVirtualRingType_Type()
)
cienaCesRapsVirtualRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingType.setStatus("current")


class _CienaCesRapsVirtualRingSubRingPortTerm_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingSubRingPortTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTerminate", 1),
          ("westPortTerminate", 2),
          ("eastPortTerminate", 3))
    )


_CienaCesRapsVirtualRingSubRingPortTerm_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingSubRingPortTerm_Object = MibTableColumn
cienaCesRapsVirtualRingSubRingPortTerm = _CienaCesRapsVirtualRingSubRingPortTerm_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 36),
    _CienaCesRapsVirtualRingSubRingPortTerm_Type()
)
cienaCesRapsVirtualRingSubRingPortTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingSubRingPortTerm.setStatus("current")


class _CienaCesRapsVirtualRingNotifIndex_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingNotifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_CienaCesRapsVirtualRingNotifIndex_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingNotifIndex_Object = MibTableColumn
cienaCesRapsVirtualRingNotifIndex = _CienaCesRapsVirtualRingNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 37),
    _CienaCesRapsVirtualRingNotifIndex_Type()
)
cienaCesRapsVirtualRingNotifIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingNotifIndex.setStatus("current")


class _CienaCesRapsVirtualRingAlarmExtended_Type(OctetString):
    """Custom type cienaCesRapsVirtualRingAlarmExtended based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_CienaCesRapsVirtualRingAlarmExtended_Type.__name__ = "OctetString"
_CienaCesRapsVirtualRingAlarmExtended_Object = MibTableColumn
cienaCesRapsVirtualRingAlarmExtended = _CienaCesRapsVirtualRingAlarmExtended_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 38),
    _CienaCesRapsVirtualRingAlarmExtended_Type()
)
cienaCesRapsVirtualRingAlarmExtended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingAlarmExtended.setStatus("current")


class _CienaCesRapsVirtualRingWestForce_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingWestForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsVirtualRingWestForce_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingWestForce_Object = MibTableColumn
cienaCesRapsVirtualRingWestForce = _CienaCesRapsVirtualRingWestForce_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 39),
    _CienaCesRapsVirtualRingWestForce_Type()
)
cienaCesRapsVirtualRingWestForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingWestForce.setStatus("current")


class _CienaCesRapsVirtualRingEastForce_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingEastForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsVirtualRingEastForce_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingEastForce_Object = MibTableColumn
cienaCesRapsVirtualRingEastForce = _CienaCesRapsVirtualRingEastForce_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 40),
    _CienaCesRapsVirtualRingEastForce_Type()
)
cienaCesRapsVirtualRingEastForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingEastForce.setStatus("current")


class _CienaCesRapsVirtualRingFlushPropagate_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingFlushPropagate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CienaCesRapsVirtualRingFlushPropagate_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingFlushPropagate_Object = MibTableColumn
cienaCesRapsVirtualRingFlushPropagate = _CienaCesRapsVirtualRingFlushPropagate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 41),
    _CienaCesRapsVirtualRingFlushPropagate_Type()
)
cienaCesRapsVirtualRingFlushPropagate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingFlushPropagate.setStatus("current")


class _CienaCesRapsVirtualRingLogicalRingName_Type(DisplayString):
    """Custom type cienaCesRapsVirtualRingLogicalRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CienaCesRapsVirtualRingLogicalRingName_Type.__name__ = "DisplayString"
_CienaCesRapsVirtualRingLogicalRingName_Object = MibTableColumn
cienaCesRapsVirtualRingLogicalRingName = _CienaCesRapsVirtualRingLogicalRingName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 3, 1, 1, 42),
    _CienaCesRapsVirtualRingLogicalRingName_Type()
)
cienaCesRapsVirtualRingLogicalRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingLogicalRingName.setStatus("current")
_CienaCesRapsVirtualRingMember_ObjectIdentity = ObjectIdentity
cienaCesRapsVirtualRingMember = _CienaCesRapsVirtualRingMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 4)
)
_CienaCesRapsVirtualRingMemberTable_Object = MibTable
cienaCesRapsVirtualRingMemberTable = _CienaCesRapsVirtualRingMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingMemberTable.setStatus("current")
_CienaCesRapsVirtualRingMemberEntry_Object = MibTableRow
cienaCesRapsVirtualRingMemberEntry = _CienaCesRapsVirtualRingMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 4, 1, 1)
)
cienaCesRapsVirtualRingMemberEntry.setIndexNames(
    (0, "CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingIndex"),
    (0, "CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingMemberVsId"),
)
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingMemberEntry.setStatus("current")


class _CienaCesRapsVirtualRingMemberVsId_Type(Integer32):
    """Custom type cienaCesRapsVirtualRingMemberVsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesRapsVirtualRingMemberVsId_Type.__name__ = "Integer32"
_CienaCesRapsVirtualRingMemberVsId_Object = MibTableColumn
cienaCesRapsVirtualRingMemberVsId = _CienaCesRapsVirtualRingMemberVsId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 1, 4, 1, 1, 2),
    _CienaCesRapsVirtualRingMemberVsId_Type()
)
cienaCesRapsVirtualRingMemberVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesRapsVirtualRingMemberVsId.setStatus("current")
_CienaCesRapsMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBConformance = _CienaCesRapsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 2)
)
_CienaCesRapsMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBCompliances = _CienaCesRapsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 2, 1)
)
_CienaCesRapsMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBGroups = _CienaCesRapsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 20, 2, 2)
)
_CienaCesRapsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBNotificationPrefix = _CienaCesRapsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18)
)
_CienaCesRapsMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesRapsMIBNotifications = _CienaCesRapsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0)
)

# Managed Objects groups


# Notification objects

cienaCesRapsAlarmClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0, 1)
)
cienaCesRapsAlarmClearNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingNotifIndex"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingName"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingAlarm"))
)
if mibBuilder.loadTexts:
    cienaCesRapsAlarmClearNotification.setStatus(
        "current"
    )

cienaCesRapsAlarmProtectionSwitchingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0, 2)
)
cienaCesRapsAlarmProtectionSwitchingNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingNotifIndex"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingName"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingAlarm"))
)
if mibBuilder.loadTexts:
    cienaCesRapsAlarmProtectionSwitchingNotification.setStatus(
        "current"
    )

cienaCesRapsAlarmProvisionMismatchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0, 3)
)
cienaCesRapsAlarmProvisionMismatchNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingNotifIndex"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingName"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingAlarm"))
)
if mibBuilder.loadTexts:
    cienaCesRapsAlarmProvisionMismatchNotification.setStatus(
        "current"
    )

cienaCesRapsAlarmNoRapsPduReceivedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0, 4)
)
cienaCesRapsAlarmNoRapsPduReceivedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingNotifIndex"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingName"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingAlarm"))
)
if mibBuilder.loadTexts:
    cienaCesRapsAlarmNoRapsPduReceivedNotification.setStatus(
        "current"
    )

cienaCesRapsAlarmNoRplOwnerDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 18, 0, 5)
)
cienaCesRapsAlarmNoRplOwnerDetectedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingNotifIndex"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingName"),
        ("CIENA-CES-RAPS-MIB", "cienaCesRapsVirtualRingAlarmExtended"))
)
if mibBuilder.loadTexts:
    cienaCesRapsAlarmNoRplOwnerDetectedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-RAPS-MIB",
    **{"cienaCesRapsMIB": cienaCesRapsMIB,
       "cienaCesRapsMIBObjects": cienaCesRapsMIBObjects,
       "cienaCesRapsGlobal": cienaCesRapsGlobal,
       "cienaCesRapsGlobalAttrs": cienaCesRapsGlobalAttrs,
       "cienaCesRapsState": cienaCesRapsState,
       "cienaCesRapsNodeId": cienaCesRapsNodeId,
       "cienaCesRapsEtherType": cienaCesRapsEtherType,
       "cienaCesRapsNumberOfRings": cienaCesRapsNumberOfRings,
       "cienaCesRapsLogicalRing": cienaCesRapsLogicalRing,
       "cienaCesRapsLogicalRingTable": cienaCesRapsLogicalRingTable,
       "cienaCesRapsLogicalRingEntry": cienaCesRapsLogicalRingEntry,
       "cienaCesRapsLogicalRingIndex": cienaCesRapsLogicalRingIndex,
       "cienaCesRapsLogicalRingName": cienaCesRapsLogicalRingName,
       "cienaCesRapsLogicalRingId": cienaCesRapsLogicalRingId,
       "cienaCesRapsLogicalRingGuardTime": cienaCesRapsLogicalRingGuardTime,
       "cienaCesRapsLogicalRingWtr": cienaCesRapsLogicalRingWtr,
       "cienaCesRapsLogicalRingWtb": cienaCesRapsLogicalRingWtb,
       "cienaCesRapsLogicalRingWestPortId": cienaCesRapsLogicalRingWestPortId,
       "cienaCesRapsLogicalRingWestHoldOffTime": cienaCesRapsLogicalRingWestHoldOffTime,
       "cienaCesRapsLogicalRingWestForce": cienaCesRapsLogicalRingWestForce,
       "cienaCesRapsLogicalRingWestCfmService": cienaCesRapsLogicalRingWestCfmService,
       "cienaCesRapsLogicalRingEastPortId": cienaCesRapsLogicalRingEastPortId,
       "cienaCesRapsLogicalRingEastHoldOffTime": cienaCesRapsLogicalRingEastHoldOffTime,
       "cienaCesRapsLogicalRingEastForce": cienaCesRapsLogicalRingEastForce,
       "cienaCesRapsLogicalRingEastCfmService": cienaCesRapsLogicalRingEastCfmService,
       "cienaCesRapsLogicalRingNumberOfVirtualRings": cienaCesRapsLogicalRingNumberOfVirtualRings,
       "cienaCesRapsVirtualRing": cienaCesRapsVirtualRing,
       "cienaCesRapsVirtualRingTable": cienaCesRapsVirtualRingTable,
       "cienaCesRapsVirtualRingEntry": cienaCesRapsVirtualRingEntry,
       "cienaCesRapsVirtualRingIndex": cienaCesRapsVirtualRingIndex,
       "cienaCesRapsVirtualRingName": cienaCesRapsVirtualRingName,
       "cienaCesRapsVirtualRingVid": cienaCesRapsVirtualRingVid,
       "cienaCesRapsVirtualRingLogicalRingId": cienaCesRapsVirtualRingLogicalRingId,
       "cienaCesRapsVirtualRingMel": cienaCesRapsVirtualRingMel,
       "cienaCesRapsVirtualRingRevertive": cienaCesRapsVirtualRingRevertive,
       "cienaCesRapsVirtualRingState": cienaCesRapsVirtualRingState,
       "cienaCesRapsVirtualRingStatus": cienaCesRapsVirtualRingStatus,
       "cienaCesRapsVirtualRingAlarm": cienaCesRapsVirtualRingAlarm,
       "cienaCesRapsVirtualRingNumOfSwitchOvers": cienaCesRapsVirtualRingNumOfSwitchOvers,
       "cienaCesRapsVirtualRingUptimeFromLastFailure": cienaCesRapsVirtualRingUptimeFromLastFailure,
       "cienaCesRapsVirtualRingTotalDownTime": cienaCesRapsVirtualRingTotalDownTime,
       "cienaCesRapsVirtualRingWestPortRpl": cienaCesRapsVirtualRingWestPortRpl,
       "cienaCesRapsVirtualRingWestPortState": cienaCesRapsVirtualRingWestPortState,
       "cienaCesRapsVirtualRingWestPortStatus": cienaCesRapsVirtualRingWestPortStatus,
       "cienaCesRapsVirtualRingWestPortNrRxd": cienaCesRapsVirtualRingWestPortNrRxd,
       "cienaCesRapsVirtualRingWestPortNrTxd": cienaCesRapsVirtualRingWestPortNrTxd,
       "cienaCesRapsVirtualRingWestPortSfRxd": cienaCesRapsVirtualRingWestPortSfRxd,
       "cienaCesRapsVirtualRingWestPortSfTxd": cienaCesRapsVirtualRingWestPortSfTxd,
       "cienaCesRapsVirtualRingWestPortFsRxd": cienaCesRapsVirtualRingWestPortFsRxd,
       "cienaCesRapsVirtualRingWestPortFsTxd": cienaCesRapsVirtualRingWestPortFsTxd,
       "cienaCesRapsVirtualRingWestPortNrRbRxd": cienaCesRapsVirtualRingWestPortNrRbRxd,
       "cienaCesRapsVirtualRingWestPortNrRbTxd": cienaCesRapsVirtualRingWestPortNrRbTxd,
       "cienaCesRapsVirtualRingEastPortRpl": cienaCesRapsVirtualRingEastPortRpl,
       "cienaCesRapsVirtualRingEastPortState": cienaCesRapsVirtualRingEastPortState,
       "cienaCesRapsVirtualRingEastPortStatus": cienaCesRapsVirtualRingEastPortStatus,
       "cienaCesRapsVirtualRingEastPortNrRxd": cienaCesRapsVirtualRingEastPortNrRxd,
       "cienaCesRapsVirtualRingEastPortNrTxd": cienaCesRapsVirtualRingEastPortNrTxd,
       "cienaCesRapsVirtualRingEastPortSfRxd": cienaCesRapsVirtualRingEastPortSfRxd,
       "cienaCesRapsVirtualRingEastPortSfTxd": cienaCesRapsVirtualRingEastPortSfTxd,
       "cienaCesRapsVirtualRingEastPortFsRxd": cienaCesRapsVirtualRingEastPortFsRxd,
       "cienaCesRapsVirtualRingEastPortFsTxd": cienaCesRapsVirtualRingEastPortFsTxd,
       "cienaCesRapsVirtualRingEastPortNrRbRxd": cienaCesRapsVirtualRingEastPortNrRbRxd,
       "cienaCesRapsVirtualRingEastPortNrRbTxd": cienaCesRapsVirtualRingEastPortNrRbTxd,
       "cienaCesRapsVirtualRingType": cienaCesRapsVirtualRingType,
       "cienaCesRapsVirtualRingSubRingPortTerm": cienaCesRapsVirtualRingSubRingPortTerm,
       "cienaCesRapsVirtualRingNotifIndex": cienaCesRapsVirtualRingNotifIndex,
       "cienaCesRapsVirtualRingAlarmExtended": cienaCesRapsVirtualRingAlarmExtended,
       "cienaCesRapsVirtualRingWestForce": cienaCesRapsVirtualRingWestForce,
       "cienaCesRapsVirtualRingEastForce": cienaCesRapsVirtualRingEastForce,
       "cienaCesRapsVirtualRingFlushPropagate": cienaCesRapsVirtualRingFlushPropagate,
       "cienaCesRapsVirtualRingLogicalRingName": cienaCesRapsVirtualRingLogicalRingName,
       "cienaCesRapsVirtualRingMember": cienaCesRapsVirtualRingMember,
       "cienaCesRapsVirtualRingMemberTable": cienaCesRapsVirtualRingMemberTable,
       "cienaCesRapsVirtualRingMemberEntry": cienaCesRapsVirtualRingMemberEntry,
       "cienaCesRapsVirtualRingMemberVsId": cienaCesRapsVirtualRingMemberVsId,
       "cienaCesRapsMIBConformance": cienaCesRapsMIBConformance,
       "cienaCesRapsMIBCompliances": cienaCesRapsMIBCompliances,
       "cienaCesRapsMIBGroups": cienaCesRapsMIBGroups,
       "cienaCesRapsMIBNotificationPrefix": cienaCesRapsMIBNotificationPrefix,
       "cienaCesRapsMIBNotifications": cienaCesRapsMIBNotifications,
       "cienaCesRapsAlarmClearNotification": cienaCesRapsAlarmClearNotification,
       "cienaCesRapsAlarmProtectionSwitchingNotification": cienaCesRapsAlarmProtectionSwitchingNotification,
       "cienaCesRapsAlarmProvisionMismatchNotification": cienaCesRapsAlarmProvisionMismatchNotification,
       "cienaCesRapsAlarmNoRapsPduReceivedNotification": cienaCesRapsAlarmNoRapsPduReceivedNotification,
       "cienaCesRapsAlarmNoRplOwnerDetectedNotification": cienaCesRapsAlarmNoRplOwnerDetectedNotification}
)
