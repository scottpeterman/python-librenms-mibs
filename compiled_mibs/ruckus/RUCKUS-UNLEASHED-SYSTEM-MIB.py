# SNMP MIB module (RUCKUS-UNLEASHED-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ruckus\RUCKUS-UNLEASHED-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:56 2025
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

(ruckusUnleashedSystemModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusUnleashedSystemModule")

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

ruckusUnleashedSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusUnleashedSystemObjects_ObjectIdentity = ObjectIdentity
ruckusUnleashedSystemObjects = _RuckusUnleashedSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1)
)
_RuckusUnleashedSystemInfo_ObjectIdentity = ObjectIdentity
ruckusUnleashedSystemInfo = _RuckusUnleashedSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1)
)


class _RuckusUnleashedSystemName_Type(DisplayString):
    """Custom type ruckusUnleashedSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusUnleashedSystemName_Type.__name__ = "DisplayString"
_RuckusUnleashedSystemName_Object = MibScalar
ruckusUnleashedSystemName = _RuckusUnleashedSystemName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 1),
    _RuckusUnleashedSystemName_Type()
)
ruckusUnleashedSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemName.setStatus("current")
_RuckusUnleashedSystemIPAddr_Type = IpAddress
_RuckusUnleashedSystemIPAddr_Object = MibScalar
ruckusUnleashedSystemIPAddr = _RuckusUnleashedSystemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 2),
    _RuckusUnleashedSystemIPAddr_Type()
)
ruckusUnleashedSystemIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemIPAddr.setStatus("current")


class _RuckusUnleashedSystemMacAddr_Type(OctetString):
    """Custom type ruckusUnleashedSystemMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RuckusUnleashedSystemMacAddr_Type.__name__ = "OctetString"
_RuckusUnleashedSystemMacAddr_Object = MibScalar
ruckusUnleashedSystemMacAddr = _RuckusUnleashedSystemMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 3),
    _RuckusUnleashedSystemMacAddr_Type()
)
ruckusUnleashedSystemMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemMacAddr.setStatus("current")
_RuckusUnleashedSystemUptime_Type = TimeTicks
_RuckusUnleashedSystemUptime_Object = MibScalar
ruckusUnleashedSystemUptime = _RuckusUnleashedSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 8),
    _RuckusUnleashedSystemUptime_Type()
)
ruckusUnleashedSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemUptime.setStatus("current")
_RuckusUnleashedSystemModel_Type = DisplayString
_RuckusUnleashedSystemModel_Object = MibScalar
ruckusUnleashedSystemModel = _RuckusUnleashedSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 9),
    _RuckusUnleashedSystemModel_Type()
)
ruckusUnleashedSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemModel.setStatus("current")
_RuckusUnleashedSystemLicensedAPs_Type = Unsigned32
_RuckusUnleashedSystemLicensedAPs_Object = MibScalar
ruckusUnleashedSystemLicensedAPs = _RuckusUnleashedSystemLicensedAPs_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 12),
    _RuckusUnleashedSystemLicensedAPs_Type()
)
ruckusUnleashedSystemLicensedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemLicensedAPs.setStatus("current")
_RuckusUnleashedSystemMaxSta_Type = Unsigned32
_RuckusUnleashedSystemMaxSta_Object = MibScalar
ruckusUnleashedSystemMaxSta = _RuckusUnleashedSystemMaxSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 13),
    _RuckusUnleashedSystemMaxSta_Type()
)
ruckusUnleashedSystemMaxSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemMaxSta.setStatus("current")
_RuckusUnleashedSystemSerialNumber_Type = DisplayString
_RuckusUnleashedSystemSerialNumber_Object = MibScalar
ruckusUnleashedSystemSerialNumber = _RuckusUnleashedSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 15),
    _RuckusUnleashedSystemSerialNumber_Type()
)
ruckusUnleashedSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemSerialNumber.setStatus("current")
_RuckusUnleashedSystemVersion_Type = DisplayString
_RuckusUnleashedSystemVersion_Object = MibScalar
ruckusUnleashedSystemVersion = _RuckusUnleashedSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 18),
    _RuckusUnleashedSystemVersion_Type()
)
ruckusUnleashedSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemVersion.setStatus("current")


class _RuckusUnleashedSystemCountryCode_Type(OctetString):
    """Custom type ruckusUnleashedSystemCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RuckusUnleashedSystemCountryCode_Type.__name__ = "OctetString"
_RuckusUnleashedSystemCountryCode_Object = MibScalar
ruckusUnleashedSystemCountryCode = _RuckusUnleashedSystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 1, 20),
    _RuckusUnleashedSystemCountryCode_Type()
)
ruckusUnleashedSystemCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemCountryCode.setStatus("current")
_RuckusUnleashedSystemStats_ObjectIdentity = ObjectIdentity
ruckusUnleashedSystemStats = _RuckusUnleashedSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15)
)
_RuckusUnleashedSystemStatsNumAP_Type = Unsigned32
_RuckusUnleashedSystemStatsNumAP_Object = MibScalar
ruckusUnleashedSystemStatsNumAP = _RuckusUnleashedSystemStatsNumAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 1),
    _RuckusUnleashedSystemStatsNumAP_Type()
)
ruckusUnleashedSystemStatsNumAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsNumAP.setStatus("current")
_RuckusUnleashedSystemStatsNumSta_Type = Unsigned32
_RuckusUnleashedSystemStatsNumSta_Object = MibScalar
ruckusUnleashedSystemStatsNumSta = _RuckusUnleashedSystemStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 2),
    _RuckusUnleashedSystemStatsNumSta_Type()
)
ruckusUnleashedSystemStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsNumSta.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalRxPkts_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalRxPkts_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalRxPkts = _RuckusUnleashedSystemStatsWLANTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 5),
    _RuckusUnleashedSystemStatsWLANTotalRxPkts_Type()
)
ruckusUnleashedSystemStatsWLANTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalRxPkts.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalRxBytes_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalRxBytes_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalRxBytes = _RuckusUnleashedSystemStatsWLANTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 6),
    _RuckusUnleashedSystemStatsWLANTotalRxBytes_Type()
)
ruckusUnleashedSystemStatsWLANTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalRxBytes.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalRxMulticast_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalRxMulticast_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalRxMulticast = _RuckusUnleashedSystemStatsWLANTotalRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 7),
    _RuckusUnleashedSystemStatsWLANTotalRxMulticast_Type()
)
ruckusUnleashedSystemStatsWLANTotalRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalRxMulticast.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxPkts_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxPkts_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxPkts = _RuckusUnleashedSystemStatsWLANTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 8),
    _RuckusUnleashedSystemStatsWLANTotalTxPkts_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxPkts.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxBytes_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxBytes_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxBytes = _RuckusUnleashedSystemStatsWLANTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 9),
    _RuckusUnleashedSystemStatsWLANTotalTxBytes_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxBytes.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxMulticast_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxMulticast_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxMulticast = _RuckusUnleashedSystemStatsWLANTotalTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 10),
    _RuckusUnleashedSystemStatsWLANTotalTxMulticast_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxMulticast.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxFail_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxFail_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxFail = _RuckusUnleashedSystemStatsWLANTotalTxFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 11),
    _RuckusUnleashedSystemStatsWLANTotalTxFail_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxFail.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxRetry_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxRetry_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxRetry = _RuckusUnleashedSystemStatsWLANTotalTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 12),
    _RuckusUnleashedSystemStatsWLANTotalTxRetry_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxRetry.setStatus("current")
_RuckusUnleashedSystemStatsCPUUtil_Type = Unsigned32
_RuckusUnleashedSystemStatsCPUUtil_Object = MibScalar
ruckusUnleashedSystemStatsCPUUtil = _RuckusUnleashedSystemStatsCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 13),
    _RuckusUnleashedSystemStatsCPUUtil_Type()
)
ruckusUnleashedSystemStatsCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsCPUUtil.setStatus("current")
_RuckusUnleashedSystemStatsMemoryUtil_Type = Unsigned32
_RuckusUnleashedSystemStatsMemoryUtil_Object = MibScalar
ruckusUnleashedSystemStatsMemoryUtil = _RuckusUnleashedSystemStatsMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 14),
    _RuckusUnleashedSystemStatsMemoryUtil_Type()
)
ruckusUnleashedSystemStatsMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsMemoryUtil.setStatus("current")
_RuckusUnleashedSystemStatsNumRegisteredAP_Type = Unsigned32
_RuckusUnleashedSystemStatsNumRegisteredAP_Object = MibScalar
ruckusUnleashedSystemStatsNumRegisteredAP = _RuckusUnleashedSystemStatsNumRegisteredAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 15),
    _RuckusUnleashedSystemStatsNumRegisteredAP_Type()
)
ruckusUnleashedSystemStatsNumRegisteredAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsNumRegisteredAP.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalAssocFail_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalAssocFail_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalAssocFail = _RuckusUnleashedSystemStatsWLANTotalAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 16),
    _RuckusUnleashedSystemStatsWLANTotalAssocFail_Type()
)
ruckusUnleashedSystemStatsWLANTotalAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalAssocFail.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalRxErrFrm_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalRxErrFrm_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalRxErrFrm = _RuckusUnleashedSystemStatsWLANTotalRxErrFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 17),
    _RuckusUnleashedSystemStatsWLANTotalRxErrFrm_Type()
)
ruckusUnleashedSystemStatsWLANTotalRxErrFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalRxErrFrm.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxDroppedPkt_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxDroppedPkt_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxDroppedPkt = _RuckusUnleashedSystemStatsWLANTotalTxDroppedPkt_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 19),
    _RuckusUnleashedSystemStatsWLANTotalTxDroppedPkt_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxDroppedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxDroppedPkt.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxErrFrm_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxErrFrm_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxErrFrm = _RuckusUnleashedSystemStatsWLANTotalTxErrFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 20),
    _RuckusUnleashedSystemStatsWLANTotalTxErrFrm_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxErrFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxErrFrm.setStatus("current")
_RuckusUnleashedSystemStatsWLANTotalTxDroppedFrm_Type = Counter64
_RuckusUnleashedSystemStatsWLANTotalTxDroppedFrm_Object = MibScalar
ruckusUnleashedSystemStatsWLANTotalTxDroppedFrm = _RuckusUnleashedSystemStatsWLANTotalTxDroppedFrm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 21),
    _RuckusUnleashedSystemStatsWLANTotalTxDroppedFrm_Type()
)
ruckusUnleashedSystemStatsWLANTotalTxDroppedFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsWLANTotalTxDroppedFrm.setStatus("current")
_RuckusUnleashedSystemStatsAllNumSta_Type = Unsigned32
_RuckusUnleashedSystemStatsAllNumSta_Object = MibScalar
ruckusUnleashedSystemStatsAllNumSta = _RuckusUnleashedSystemStatsAllNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 15, 1, 1, 1, 15, 30),
    _RuckusUnleashedSystemStatsAllNumSta_Type()
)
ruckusUnleashedSystemStatsAllNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusUnleashedSystemStatsAllNumSta.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-UNLEASHED-SYSTEM-MIB",
    **{"ruckusUnleashedSystemMIB": ruckusUnleashedSystemMIB,
       "ruckusUnleashedSystemObjects": ruckusUnleashedSystemObjects,
       "ruckusUnleashedSystemInfo": ruckusUnleashedSystemInfo,
       "ruckusUnleashedSystemName": ruckusUnleashedSystemName,
       "ruckusUnleashedSystemIPAddr": ruckusUnleashedSystemIPAddr,
       "ruckusUnleashedSystemMacAddr": ruckusUnleashedSystemMacAddr,
       "ruckusUnleashedSystemUptime": ruckusUnleashedSystemUptime,
       "ruckusUnleashedSystemModel": ruckusUnleashedSystemModel,
       "ruckusUnleashedSystemLicensedAPs": ruckusUnleashedSystemLicensedAPs,
       "ruckusUnleashedSystemMaxSta": ruckusUnleashedSystemMaxSta,
       "ruckusUnleashedSystemSerialNumber": ruckusUnleashedSystemSerialNumber,
       "ruckusUnleashedSystemVersion": ruckusUnleashedSystemVersion,
       "ruckusUnleashedSystemCountryCode": ruckusUnleashedSystemCountryCode,
       "ruckusUnleashedSystemStats": ruckusUnleashedSystemStats,
       "ruckusUnleashedSystemStatsNumAP": ruckusUnleashedSystemStatsNumAP,
       "ruckusUnleashedSystemStatsNumSta": ruckusUnleashedSystemStatsNumSta,
       "ruckusUnleashedSystemStatsWLANTotalRxPkts": ruckusUnleashedSystemStatsWLANTotalRxPkts,
       "ruckusUnleashedSystemStatsWLANTotalRxBytes": ruckusUnleashedSystemStatsWLANTotalRxBytes,
       "ruckusUnleashedSystemStatsWLANTotalRxMulticast": ruckusUnleashedSystemStatsWLANTotalRxMulticast,
       "ruckusUnleashedSystemStatsWLANTotalTxPkts": ruckusUnleashedSystemStatsWLANTotalTxPkts,
       "ruckusUnleashedSystemStatsWLANTotalTxBytes": ruckusUnleashedSystemStatsWLANTotalTxBytes,
       "ruckusUnleashedSystemStatsWLANTotalTxMulticast": ruckusUnleashedSystemStatsWLANTotalTxMulticast,
       "ruckusUnleashedSystemStatsWLANTotalTxFail": ruckusUnleashedSystemStatsWLANTotalTxFail,
       "ruckusUnleashedSystemStatsWLANTotalTxRetry": ruckusUnleashedSystemStatsWLANTotalTxRetry,
       "ruckusUnleashedSystemStatsCPUUtil": ruckusUnleashedSystemStatsCPUUtil,
       "ruckusUnleashedSystemStatsMemoryUtil": ruckusUnleashedSystemStatsMemoryUtil,
       "ruckusUnleashedSystemStatsNumRegisteredAP": ruckusUnleashedSystemStatsNumRegisteredAP,
       "ruckusUnleashedSystemStatsWLANTotalAssocFail": ruckusUnleashedSystemStatsWLANTotalAssocFail,
       "ruckusUnleashedSystemStatsWLANTotalRxErrFrm": ruckusUnleashedSystemStatsWLANTotalRxErrFrm,
       "ruckusUnleashedSystemStatsWLANTotalTxDroppedPkt": ruckusUnleashedSystemStatsWLANTotalTxDroppedPkt,
       "ruckusUnleashedSystemStatsWLANTotalTxErrFrm": ruckusUnleashedSystemStatsWLANTotalTxErrFrm,
       "ruckusUnleashedSystemStatsWLANTotalTxDroppedFrm": ruckusUnleashedSystemStatsWLANTotalTxDroppedFrm,
       "ruckusUnleashedSystemStatsAllNumSta": ruckusUnleashedSystemStatsAllNumSta}
)
