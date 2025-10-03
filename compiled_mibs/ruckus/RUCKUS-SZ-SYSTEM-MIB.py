# SNMP MIB module (RUCKUS-SZ-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-SZ-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:49 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusSZSystemModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSZSystemModule")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusSZSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSZSystemObjects_ObjectIdentity = ObjectIdentity
ruckusSZSystemObjects = _RuckusSZSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1)
)
_RuckusSZSystemInfo_ObjectIdentity = ObjectIdentity
ruckusSZSystemInfo = _RuckusSZSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 1)
)
_RuckusSZSystemStats_ObjectIdentity = ObjectIdentity
ruckusSZSystemStats = _RuckusSZSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15)
)
_RuckusSZSystemStatsNumAP_Type = Unsigned32
_RuckusSZSystemStatsNumAP_Object = MibScalar
ruckusSZSystemStatsNumAP = _RuckusSZSystemStatsNumAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 1),
    _RuckusSZSystemStatsNumAP_Type()
)
ruckusSZSystemStatsNumAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsNumAP.setStatus("current")
_RuckusSZSystemStatsNumSta_Type = Unsigned32
_RuckusSZSystemStatsNumSta_Object = MibScalar
ruckusSZSystemStatsNumSta = _RuckusSZSystemStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 2),
    _RuckusSZSystemStatsNumSta_Type()
)
ruckusSZSystemStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsNumSta.setStatus("current")
_RuckusSZSystemStatsWLANTotalRxPkts_Type = Counter64
_RuckusSZSystemStatsWLANTotalRxPkts_Object = MibScalar
ruckusSZSystemStatsWLANTotalRxPkts = _RuckusSZSystemStatsWLANTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 5),
    _RuckusSZSystemStatsWLANTotalRxPkts_Type()
)
ruckusSZSystemStatsWLANTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalRxPkts.setStatus("current")
_RuckusSZSystemStatsWLANTotalRxBytes_Type = Counter64
_RuckusSZSystemStatsWLANTotalRxBytes_Object = MibScalar
ruckusSZSystemStatsWLANTotalRxBytes = _RuckusSZSystemStatsWLANTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 6),
    _RuckusSZSystemStatsWLANTotalRxBytes_Type()
)
ruckusSZSystemStatsWLANTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalRxBytes.setStatus("current")
_RuckusSZSystemStatsWLANTotalRxMulticast_Type = Counter64
_RuckusSZSystemStatsWLANTotalRxMulticast_Object = MibScalar
ruckusSZSystemStatsWLANTotalRxMulticast = _RuckusSZSystemStatsWLANTotalRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 7),
    _RuckusSZSystemStatsWLANTotalRxMulticast_Type()
)
ruckusSZSystemStatsWLANTotalRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalRxMulticast.setStatus("current")
_RuckusSZSystemStatsWLANTotalTxPkts_Type = Counter64
_RuckusSZSystemStatsWLANTotalTxPkts_Object = MibScalar
ruckusSZSystemStatsWLANTotalTxPkts = _RuckusSZSystemStatsWLANTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 8),
    _RuckusSZSystemStatsWLANTotalTxPkts_Type()
)
ruckusSZSystemStatsWLANTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalTxPkts.setStatus("current")
_RuckusSZSystemStatsWLANTotalTxBytes_Type = Counter64
_RuckusSZSystemStatsWLANTotalTxBytes_Object = MibScalar
ruckusSZSystemStatsWLANTotalTxBytes = _RuckusSZSystemStatsWLANTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 9),
    _RuckusSZSystemStatsWLANTotalTxBytes_Type()
)
ruckusSZSystemStatsWLANTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalTxBytes.setStatus("current")
_RuckusSZSystemStatsWLANTotalTxMulticast_Type = Counter64
_RuckusSZSystemStatsWLANTotalTxMulticast_Object = MibScalar
ruckusSZSystemStatsWLANTotalTxMulticast = _RuckusSZSystemStatsWLANTotalTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 10),
    _RuckusSZSystemStatsWLANTotalTxMulticast_Type()
)
ruckusSZSystemStatsWLANTotalTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalTxMulticast.setStatus("current")
_RuckusSZSystemStatsWLANTotalTxFail_Type = Counter64
_RuckusSZSystemStatsWLANTotalTxFail_Object = MibScalar
ruckusSZSystemStatsWLANTotalTxFail = _RuckusSZSystemStatsWLANTotalTxFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 11),
    _RuckusSZSystemStatsWLANTotalTxFail_Type()
)
ruckusSZSystemStatsWLANTotalTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalTxFail.setStatus("current")
_RuckusSZSystemStatsWLANTotalTxRetry_Type = Counter64
_RuckusSZSystemStatsWLANTotalTxRetry_Object = MibScalar
ruckusSZSystemStatsWLANTotalTxRetry = _RuckusSZSystemStatsWLANTotalTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 12),
    _RuckusSZSystemStatsWLANTotalTxRetry_Type()
)
ruckusSZSystemStatsWLANTotalTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsWLANTotalTxRetry.setStatus("current")
_RuckusSZSystemStatsSerialNumber_Type = DisplayString
_RuckusSZSystemStatsSerialNumber_Object = MibScalar
ruckusSZSystemStatsSerialNumber = _RuckusSZSystemStatsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 4, 1, 1, 1, 15, 13),
    _RuckusSZSystemStatsSerialNumber_Type()
)
ruckusSZSystemStatsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSZSystemStatsSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SZ-SYSTEM-MIB",
    **{"ruckusSZSystemMIB": ruckusSZSystemMIB,
       "ruckusSZSystemObjects": ruckusSZSystemObjects,
       "ruckusSZSystemInfo": ruckusSZSystemInfo,
       "ruckusSZSystemStats": ruckusSZSystemStats,
       "ruckusSZSystemStatsNumAP": ruckusSZSystemStatsNumAP,
       "ruckusSZSystemStatsNumSta": ruckusSZSystemStatsNumSta,
       "ruckusSZSystemStatsWLANTotalRxPkts": ruckusSZSystemStatsWLANTotalRxPkts,
       "ruckusSZSystemStatsWLANTotalRxBytes": ruckusSZSystemStatsWLANTotalRxBytes,
       "ruckusSZSystemStatsWLANTotalRxMulticast": ruckusSZSystemStatsWLANTotalRxMulticast,
       "ruckusSZSystemStatsWLANTotalTxPkts": ruckusSZSystemStatsWLANTotalTxPkts,
       "ruckusSZSystemStatsWLANTotalTxBytes": ruckusSZSystemStatsWLANTotalTxBytes,
       "ruckusSZSystemStatsWLANTotalTxMulticast": ruckusSZSystemStatsWLANTotalTxMulticast,
       "ruckusSZSystemStatsWLANTotalTxFail": ruckusSZSystemStatsWLANTotalTxFail,
       "ruckusSZSystemStatsWLANTotalTxRetry": ruckusSZSystemStatsWLANTotalTxRetry,
       "ruckusSZSystemStatsSerialNumber": ruckusSZSystemStatsSerialNumber}
)
