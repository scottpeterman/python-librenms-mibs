# SNMP MIB module (CISCOSB-BRGMACSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-BRGMACSWITCH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:16 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlBrgMacSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50)
)
if mibBuilder.loadTexts:
    rlBrgMacSwitch.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlBrgMacSwVersion_Type = Integer32
_RlBrgMacSwVersion_Object = MibScalar
rlBrgMacSwVersion = _RlBrgMacSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 1),
    _RlBrgMacSwVersion_Type()
)
rlBrgMacSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwVersion.setStatus("current")
_RlBrgMacSwMaxTableNumber_Type = Integer32
_RlBrgMacSwMaxTableNumber_Object = MibScalar
rlBrgMacSwMaxTableNumber = _RlBrgMacSwMaxTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 2),
    _RlBrgMacSwMaxTableNumber_Type()
)
rlBrgMacSwMaxTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwMaxTableNumber.setStatus("current")


class _RlBrgMacSwDynamicTables_Type(Integer32):
    """Custom type rlBrgMacSwDynamicTables based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlBrgMacSwDynamicTables_Type.__name__ = "Integer32"
_RlBrgMacSwDynamicTables_Object = MibScalar
rlBrgMacSwDynamicTables = _RlBrgMacSwDynamicTables_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 3),
    _RlBrgMacSwDynamicTables_Type()
)
rlBrgMacSwDynamicTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwDynamicTables.setStatus("current")


class _RlBrgMacSwOldEntryDeleteMode_Type(Integer32):
    """Custom type rlBrgMacSwOldEntryDeleteMode based on Integer32"""
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
        *(("refreshFlag", 1),
          ("agingFlag", 2),
          ("agingTime", 3),
          ("boundaries", 4))
    )


_RlBrgMacSwOldEntryDeleteMode_Type.__name__ = "Integer32"
_RlBrgMacSwOldEntryDeleteMode_Object = MibScalar
rlBrgMacSwOldEntryDeleteMode = _RlBrgMacSwOldEntryDeleteMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 5),
    _RlBrgMacSwOldEntryDeleteMode_Type()
)
rlBrgMacSwOldEntryDeleteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwOldEntryDeleteMode.setStatus("current")


class _RlBrgMacSwSpanningTree_Type(Integer32):
    """Custom type rlBrgMacSwSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_RlBrgMacSwSpanningTree_Type.__name__ = "Integer32"
_RlBrgMacSwSpanningTree_Object = MibScalar
rlBrgMacSwSpanningTree = _RlBrgMacSwSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 6),
    _RlBrgMacSwSpanningTree_Type()
)
rlBrgMacSwSpanningTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwSpanningTree.setStatus("current")


class _RlBrgMacSwKeyType_Type(Integer32):
    """Custom type rlBrgMacSwKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macOnly", 1),
          ("tagAndMac", 2))
    )


_RlBrgMacSwKeyType_Type.__name__ = "Integer32"
_RlBrgMacSwKeyType_Object = MibScalar
rlBrgMacSwKeyType = _RlBrgMacSwKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 7),
    _RlBrgMacSwKeyType_Type()
)
rlBrgMacSwKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwKeyType.setStatus("current")
_RlBrgMacSwYellowBoundary_Type = Integer32
_RlBrgMacSwYellowBoundary_Object = MibScalar
rlBrgMacSwYellowBoundary = _RlBrgMacSwYellowBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 8),
    _RlBrgMacSwYellowBoundary_Type()
)
rlBrgMacSwYellowBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwYellowBoundary.setStatus("current")
_RlBrgMacSwRedBoundary_Type = Integer32
_RlBrgMacSwRedBoundary_Object = MibScalar
rlBrgMacSwRedBoundary = _RlBrgMacSwRedBoundary_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 9),
    _RlBrgMacSwRedBoundary_Type()
)
rlBrgMacSwRedBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwRedBoundary.setStatus("current")


class _RlBrgMacSwTrapEnable_Type(TruthValue):
    """Custom type rlBrgMacSwTrapEnable based on TruthValue"""
    defaultValue = 2


_RlBrgMacSwTrapEnable_Type.__name__ = "TruthValue"
_RlBrgMacSwTrapEnable_Object = MibScalar
rlBrgMacSwTrapEnable = _RlBrgMacSwTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 10),
    _RlBrgMacSwTrapEnable_Type()
)
rlBrgMacSwTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwTrapEnable.setStatus("current")
_RlBrgMacSwOperTrapCount_Type = Integer32
_RlBrgMacSwOperTrapCount_Object = MibScalar
rlBrgMacSwOperTrapCount = _RlBrgMacSwOperTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 11),
    _RlBrgMacSwOperTrapCount_Type()
)
rlBrgMacSwOperTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMacSwOperTrapCount.setStatus("current")


class _RlBrgMacSwAdminTrapFrequency_Type(Integer32):
    """Custom type rlBrgMacSwAdminTrapFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RlBrgMacSwAdminTrapFrequency_Type.__name__ = "Integer32"
_RlBrgMacSwAdminTrapFrequency_Object = MibScalar
rlBrgMacSwAdminTrapFrequency = _RlBrgMacSwAdminTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 50, 12),
    _RlBrgMacSwAdminTrapFrequency_Type()
)
rlBrgMacSwAdminTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgMacSwAdminTrapFrequency.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-BRGMACSWITCH-MIB",
    **{"rlBrgMacSwitch": rlBrgMacSwitch,
       "rlBrgMacSwVersion": rlBrgMacSwVersion,
       "rlBrgMacSwMaxTableNumber": rlBrgMacSwMaxTableNumber,
       "rlBrgMacSwDynamicTables": rlBrgMacSwDynamicTables,
       "rlBrgMacSwOldEntryDeleteMode": rlBrgMacSwOldEntryDeleteMode,
       "rlBrgMacSwSpanningTree": rlBrgMacSwSpanningTree,
       "rlBrgMacSwKeyType": rlBrgMacSwKeyType,
       "rlBrgMacSwYellowBoundary": rlBrgMacSwYellowBoundary,
       "rlBrgMacSwRedBoundary": rlBrgMacSwRedBoundary,
       "rlBrgMacSwTrapEnable": rlBrgMacSwTrapEnable,
       "rlBrgMacSwOperTrapCount": rlBrgMacSwOperTrapCount,
       "rlBrgMacSwAdminTrapFrequency": rlBrgMacSwAdminTrapFrequency}
)
