# SNMP MIB module (TN-SAT-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-SAT-LOOPBACK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:21 2025
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

(IEEE8021BridgePortNumberOrZero,
 IEEE8021VlanIndexOrWildcard) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumberOrZero",
    "IEEE8021VlanIndexOrWildcard")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnEthSatLoopbackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130)
)
if mibBuilder.loadTexts:
    tnEthSatLoopbackMIB.setRevisions(
        ("2013-03-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnEthSatLoopbackMIBNotifications_ObjectIdentity = ObjectIdentity
tnEthSatLoopbackMIBNotifications = _TnEthSatLoopbackMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 0)
)
_TnEthSatLoopbackMIBObject_ObjectIdentity = ObjectIdentity
tnEthSatLoopbackMIBObject = _TnEthSatLoopbackMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1)
)
_TnEthSatLoopBackCfgTable_Object = MibTable
tnEthSatLoopBackCfgTable = _TnEthSatLoopBackCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1)
)
if mibBuilder.loadTexts:
    tnEthSatLoopBackCfgTable.setStatus("current")
_TnEthSatLoopBackCfgEntry_Object = MibTableRow
tnEthSatLoopBackCfgEntry = _TnEthSatLoopBackCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1)
)
tnEthSatLoopBackCfgEntry.setIndexNames(
    (0, "TN-SAT-LOOPBACK-MIB", "tnEthSatLoopBackIndex"),
)
if mibBuilder.loadTexts:
    tnEthSatLoopBackCfgEntry.setStatus("current")
_TnEthSatLoopBackIndex_Type = Unsigned32
_TnEthSatLoopBackIndex_Object = MibTableColumn
tnEthSatLoopBackIndex = _TnEthSatLoopBackIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 1),
    _TnEthSatLoopBackIndex_Type()
)
tnEthSatLoopBackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnEthSatLoopBackIndex.setStatus("current")
_TnEthSatLoopBackEnabled_Type = TruthValue
_TnEthSatLoopBackEnabled_Object = MibTableColumn
tnEthSatLoopBackEnabled = _TnEthSatLoopBackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 2),
    _TnEthSatLoopBackEnabled_Type()
)
tnEthSatLoopBackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSatLoopBackEnabled.setStatus("current")
_TnEthSatLoopBackPort_Type = IEEE8021BridgePortNumberOrZero
_TnEthSatLoopBackPort_Object = MibTableColumn
tnEthSatLoopBackPort = _TnEthSatLoopBackPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 3),
    _TnEthSatLoopBackPort_Type()
)
tnEthSatLoopBackPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSatLoopBackPort.setStatus("current")
_TnEthSatLoopBackAddress_Type = MacAddress
_TnEthSatLoopBackAddress_Object = MibTableColumn
tnEthSatLoopBackAddress = _TnEthSatLoopBackAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 4),
    _TnEthSatLoopBackAddress_Type()
)
tnEthSatLoopBackAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSatLoopBackAddress.setStatus("current")
_TnEthSatLoopBackVid_Type = IEEE8021VlanIndexOrWildcard
_TnEthSatLoopBackVid_Object = MibTableColumn
tnEthSatLoopBackVid = _TnEthSatLoopBackVid_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 5),
    _TnEthSatLoopBackVid_Type()
)
tnEthSatLoopBackVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSatLoopBackVid.setStatus("current")


class _TnEthSatLoopBackTimeOut_Type(Unsigned32):
    """Custom type tnEthSatLoopBackTimeOut based on Unsigned32"""
    defaultValue = 300


_TnEthSatLoopBackTimeOut_Type.__name__ = "Unsigned32"
_TnEthSatLoopBackTimeOut_Object = MibTableColumn
tnEthSatLoopBackTimeOut = _TnEthSatLoopBackTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 1, 1, 6),
    _TnEthSatLoopBackTimeOut_Type()
)
tnEthSatLoopBackTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnEthSatLoopBackTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tnEthSatLoopBackTimeOut.setUnits("seconds")
_TnEthSatLoopBackStatsTable_Object = MibTable
tnEthSatLoopBackStatsTable = _TnEthSatLoopBackStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 2)
)
if mibBuilder.loadTexts:
    tnEthSatLoopBackStatsTable.setStatus("current")
_TnEthSatLoopBackStatsEntry_Object = MibTableRow
tnEthSatLoopBackStatsEntry = _TnEthSatLoopBackStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 2, 1)
)
tnEthSatLoopBackStatsEntry.setIndexNames(
    (0, "TN-SAT-LOOPBACK-MIB", "tnEthSatLoopBackIndex"),
)
if mibBuilder.loadTexts:
    tnEthSatLoopBackStatsEntry.setStatus("current")
_TnEthSatLoopBackTimeLeft_Type = Unsigned32
_TnEthSatLoopBackTimeLeft_Object = MibTableColumn
tnEthSatLoopBackTimeLeft = _TnEthSatLoopBackTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 2, 1, 1),
    _TnEthSatLoopBackTimeLeft_Type()
)
tnEthSatLoopBackTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSatLoopBackTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tnEthSatLoopBackTimeLeft.setUnits("seconds")
_TnEthSatLoopBackFrames_Type = Counter64
_TnEthSatLoopBackFrames_Object = MibTableColumn
tnEthSatLoopBackFrames = _TnEthSatLoopBackFrames_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 2, 1, 2),
    _TnEthSatLoopBackFrames_Type()
)
tnEthSatLoopBackFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSatLoopBackFrames.setStatus("current")
_TnEthSatLoopBackBytes_Type = Counter64
_TnEthSatLoopBackBytes_Object = MibTableColumn
tnEthSatLoopBackBytes = _TnEthSatLoopBackBytes_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 1, 2, 1, 3),
    _TnEthSatLoopBackBytes_Type()
)
tnEthSatLoopBackBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnEthSatLoopBackBytes.setStatus("current")
_TnEthSatLoopbackMIBConformance_ObjectIdentity = ObjectIdentity
tnEthSatLoopbackMIBConformance = _TnEthSatLoopbackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 130, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAT-LOOPBACK-MIB",
    **{"tnEthSatLoopbackMIB": tnEthSatLoopbackMIB,
       "tnEthSatLoopbackMIBNotifications": tnEthSatLoopbackMIBNotifications,
       "tnEthSatLoopbackMIBObject": tnEthSatLoopbackMIBObject,
       "tnEthSatLoopBackCfgTable": tnEthSatLoopBackCfgTable,
       "tnEthSatLoopBackCfgEntry": tnEthSatLoopBackCfgEntry,
       "tnEthSatLoopBackIndex": tnEthSatLoopBackIndex,
       "tnEthSatLoopBackEnabled": tnEthSatLoopBackEnabled,
       "tnEthSatLoopBackPort": tnEthSatLoopBackPort,
       "tnEthSatLoopBackAddress": tnEthSatLoopBackAddress,
       "tnEthSatLoopBackVid": tnEthSatLoopBackVid,
       "tnEthSatLoopBackTimeOut": tnEthSatLoopBackTimeOut,
       "tnEthSatLoopBackStatsTable": tnEthSatLoopBackStatsTable,
       "tnEthSatLoopBackStatsEntry": tnEthSatLoopBackStatsEntry,
       "tnEthSatLoopBackTimeLeft": tnEthSatLoopBackTimeLeft,
       "tnEthSatLoopBackFrames": tnEthSatLoopBackFrames,
       "tnEthSatLoopBackBytes": tnEthSatLoopBackBytes,
       "tnEthSatLoopbackMIBConformance": tnEthSatLoopbackMIBConformance}
)
