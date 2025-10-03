# SNMP MIB module (DLINKSW-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:50 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(Dlink2kVlanList,) = mibBuilder.importSymbols(
    "DLINKSW-TC-MIB",
    "Dlink2kVlanList")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwDhcpRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23)
)
if mibBuilder.loadTexts:
    dlinkSwDhcpRelayMIB.setRevisions(
        ("2013-07-19 00:00",
         "2013-09-09 00:00",
         "2013-09-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DDhcpRelayMIBNotifications_ObjectIdentity = ObjectIdentity
dDhcpRelayMIBNotifications = _DDhcpRelayMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 0)
)
_DDhcpRelayMIBObjects_ObjectIdentity = ObjectIdentity
dDhcpRelayMIBObjects = _DDhcpRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1)
)
_DDhcpRelayGeneral_ObjectIdentity = ObjectIdentity
dDhcpRelayGeneral = _DDhcpRelayGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1)
)


class _DDhcpRelayAgentInfoCheckEnabled_Type(TruthValue):
    """Custom type dDhcpRelayAgentInfoCheckEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpRelayAgentInfoCheckEnabled_Type.__name__ = "TruthValue"
_DDhcpRelayAgentInfoCheckEnabled_Object = MibScalar
dDhcpRelayAgentInfoCheckEnabled = _DDhcpRelayAgentInfoCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 1),
    _DDhcpRelayAgentInfoCheckEnabled_Type()
)
dDhcpRelayAgentInfoCheckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRelayAgentInfoCheckEnabled.setStatus("current")


class _DDhcpRelayAgentInfoInsertEnabled_Type(TruthValue):
    """Custom type dDhcpRelayAgentInfoInsertEnabled based on TruthValue"""
    defaultValue = 2


_DDhcpRelayAgentInfoInsertEnabled_Type.__name__ = "TruthValue"
_DDhcpRelayAgentInfoInsertEnabled_Object = MibScalar
dDhcpRelayAgentInfoInsertEnabled = _DDhcpRelayAgentInfoInsertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 2),
    _DDhcpRelayAgentInfoInsertEnabled_Type()
)
dDhcpRelayAgentInfoInsertEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRelayAgentInfoInsertEnabled.setStatus("current")


class _DDhcpRelayAgentInfoPolicy_Type(Integer32):
    """Custom type dDhcpRelayAgentInfoPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_DDhcpRelayAgentInfoPolicy_Type.__name__ = "Integer32"
_DDhcpRelayAgentInfoPolicy_Object = MibScalar
dDhcpRelayAgentInfoPolicy = _DDhcpRelayAgentInfoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 3),
    _DDhcpRelayAgentInfoPolicy_Type()
)
dDhcpRelayAgentInfoPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRelayAgentInfoPolicy.setStatus("current")


class _DDhcpRelayInfoTrustAll_Type(TruthValue):
    """Custom type dDhcpRelayInfoTrustAll based on TruthValue"""
    defaultValue = 2


_DDhcpRelayInfoTrustAll_Type.__name__ = "TruthValue"
_DDhcpRelayInfoTrustAll_Object = MibScalar
dDhcpRelayInfoTrustAll = _DDhcpRelayInfoTrustAll_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 4),
    _DDhcpRelayInfoTrustAll_Type()
)
dDhcpRelayInfoTrustAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRelayInfoTrustAll.setStatus("current")


class _DDhcpRelaySmartRelay_Type(TruthValue):
    """Custom type dDhcpRelaySmartRelay based on TruthValue"""
    defaultValue = 2


_DDhcpRelaySmartRelay_Type.__name__ = "TruthValue"
_DDhcpRelaySmartRelay_Object = MibScalar
dDhcpRelaySmartRelay = _DDhcpRelaySmartRelay_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 5),
    _DDhcpRelaySmartRelay_Type()
)
dDhcpRelaySmartRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRelaySmartRelay.setStatus("current")


class _DDhcpROption82RemoteIdType_Type(Integer32):
    """Custom type dDhcpROption82RemoteIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("userDefined", 2),
          ("vendor2", 4),
          ("vendor3", 5))
    )


_DDhcpROption82RemoteIdType_Type.__name__ = "Integer32"
_DDhcpROption82RemoteIdType_Object = MibScalar
dDhcpROption82RemoteIdType = _DDhcpROption82RemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 6),
    _DDhcpROption82RemoteIdType_Type()
)
dDhcpROption82RemoteIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpROption82RemoteIdType.setStatus("current")


class _DDhcpROption82RemoteIdUserDef_Type(DisplayString):
    """Custom type dDhcpROption82RemoteIdUserDef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpROption82RemoteIdUserDef_Type.__name__ = "DisplayString"
_DDhcpROption82RemoteIdUserDef_Object = MibScalar
dDhcpROption82RemoteIdUserDef = _DDhcpROption82RemoteIdUserDef_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 7),
    _DDhcpROption82RemoteIdUserDef_Type()
)
dDhcpROption82RemoteIdUserDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpROption82RemoteIdUserDef.setStatus("current")


class _DDhcpROption82CircuitIdType_Type(Integer32):
    """Custom type dDhcpROption82CircuitIdType based on Integer32"""
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
        *(("default", 1),
          ("userDefined", 2),
          ("vendor1", 3),
          ("vendor2", 4),
          ("vendor3", 5),
          ("vendor4", 6),
          ("vendor5", 7),
          ("vendor6", 8))
    )


_DDhcpROption82CircuitIdType_Type.__name__ = "Integer32"
_DDhcpROption82CircuitIdType_Object = MibScalar
dDhcpROption82CircuitIdType = _DDhcpROption82CircuitIdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 8),
    _DDhcpROption82CircuitIdType_Type()
)
dDhcpROption82CircuitIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpROption82CircuitIdType.setStatus("current")


class _DDhcpROption82CircuitIdUserDef_Type(DisplayString):
    """Custom type dDhcpROption82CircuitIdUserDef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpROption82CircuitIdUserDef_Type.__name__ = "DisplayString"
_DDhcpROption82CircuitIdUserDef_Object = MibScalar
dDhcpROption82CircuitIdUserDef = _DDhcpROption82CircuitIdUserDef_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 1, 9),
    _DDhcpROption82CircuitIdUserDef_Type()
)
dDhcpROption82CircuitIdUserDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpROption82CircuitIdUserDef.setStatus("current")
_DDhcpRPoolObjects_ObjectIdentity = ObjectIdentity
dDhcpRPoolObjects = _DDhcpRPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2)
)
_DDhcpRPoolClassRelayTargetTable_Object = MibTable
dDhcpRPoolClassRelayTargetTable = _DDhcpRPoolClassRelayTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dDhcpRPoolClassRelayTargetTable.setStatus("current")
_DDhcpRPoolClassRelayTargetEntry_Object = MibTableRow
dDhcpRPoolClassRelayTargetEntry = _DDhcpRPoolClassRelayTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1)
)
dDhcpRPoolClassRelayTargetEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoClRelayTargetPoolName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoClRelayTargetClassName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoClRelayTargetVrfName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoClRelayTargetAddr"),
)
if mibBuilder.loadTexts:
    dDhcpRPoolClassRelayTargetEntry.setStatus("current")


class _DDhcpRPoClRelayTargetPoolName_Type(DisplayString):
    """Custom type dDhcpRPoClRelayTargetPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcpRPoClRelayTargetPoolName_Type.__name__ = "DisplayString"
_DDhcpRPoClRelayTargetPoolName_Object = MibTableColumn
dDhcpRPoClRelayTargetPoolName = _DDhcpRPoClRelayTargetPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1, 1),
    _DDhcpRPoClRelayTargetPoolName_Type()
)
dDhcpRPoClRelayTargetPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoClRelayTargetPoolName.setStatus("current")


class _DDhcpRPoClRelayTargetClassName_Type(DisplayString):
    """Custom type dDhcpRPoClRelayTargetClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcpRPoClRelayTargetClassName_Type.__name__ = "DisplayString"
_DDhcpRPoClRelayTargetClassName_Object = MibTableColumn
dDhcpRPoClRelayTargetClassName = _DDhcpRPoClRelayTargetClassName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1, 2),
    _DDhcpRPoClRelayTargetClassName_Type()
)
dDhcpRPoClRelayTargetClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoClRelayTargetClassName.setStatus("current")


class _DDhcpRPoClRelayTargetVrfName_Type(DisplayString):
    """Custom type dDhcpRPoClRelayTargetVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpRPoClRelayTargetVrfName_Type.__name__ = "DisplayString"
_DDhcpRPoClRelayTargetVrfName_Object = MibTableColumn
dDhcpRPoClRelayTargetVrfName = _DDhcpRPoClRelayTargetVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1, 3),
    _DDhcpRPoClRelayTargetVrfName_Type()
)
dDhcpRPoClRelayTargetVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoClRelayTargetVrfName.setStatus("current")
_DDhcpRPoClRelayTargetAddr_Type = IpAddress
_DDhcpRPoClRelayTargetAddr_Object = MibTableColumn
dDhcpRPoClRelayTargetAddr = _DDhcpRPoClRelayTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1, 4),
    _DDhcpRPoClRelayTargetAddr_Type()
)
dDhcpRPoClRelayTargetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoClRelayTargetAddr.setStatus("current")
_DDhcpRPoClRelayTargetRowStatus_Type = RowStatus
_DDhcpRPoClRelayTargetRowStatus_Object = MibTableColumn
dDhcpRPoClRelayTargetRowStatus = _DDhcpRPoClRelayTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 1, 1, 99),
    _DDhcpRPoClRelayTargetRowStatus_Type()
)
dDhcpRPoClRelayTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRPoClRelayTargetRowStatus.setStatus("current")
_DDhcpRPoolRelayDestTable_Object = MibTable
dDhcpRPoolRelayDestTable = _DDhcpRPoolRelayDestTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestTable.setStatus("current")
_DDhcpRPoolRelayDestEntry_Object = MibTableRow
dDhcpRPoolRelayDestEntry = _DDhcpRPoolRelayDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2, 1)
)
dDhcpRPoolRelayDestEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelayDestPoolName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelayDestVrfName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelayDestAddr"),
)
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestEntry.setStatus("current")


class _DDhcpRPoolRelayDestPoolName_Type(DisplayString):
    """Custom type dDhcpRPoolRelayDestPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DDhcpRPoolRelayDestPoolName_Type.__name__ = "DisplayString"
_DDhcpRPoolRelayDestPoolName_Object = MibTableColumn
dDhcpRPoolRelayDestPoolName = _DDhcpRPoolRelayDestPoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2, 1, 1),
    _DDhcpRPoolRelayDestPoolName_Type()
)
dDhcpRPoolRelayDestPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestPoolName.setStatus("current")


class _DDhcpRPoolRelayDestVrfName_Type(DisplayString):
    """Custom type dDhcpRPoolRelayDestVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpRPoolRelayDestVrfName_Type.__name__ = "DisplayString"
_DDhcpRPoolRelayDestVrfName_Object = MibTableColumn
dDhcpRPoolRelayDestVrfName = _DDhcpRPoolRelayDestVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2, 1, 2),
    _DDhcpRPoolRelayDestVrfName_Type()
)
dDhcpRPoolRelayDestVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestVrfName.setStatus("current")
_DDhcpRPoolRelayDestAddr_Type = IpAddress
_DDhcpRPoolRelayDestAddr_Object = MibTableColumn
dDhcpRPoolRelayDestAddr = _DDhcpRPoolRelayDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2, 1, 3),
    _DDhcpRPoolRelayDestAddr_Type()
)
dDhcpRPoolRelayDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestAddr.setStatus("current")
_DDhcpRPoolRelayDestRowStatus_Type = RowStatus
_DDhcpRPoolRelayDestRowStatus_Object = MibTableColumn
dDhcpRPoolRelayDestRowStatus = _DDhcpRPoolRelayDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 2, 1, 99),
    _DDhcpRPoolRelayDestRowStatus_Type()
)
dDhcpRPoolRelayDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRPoolRelayDestRowStatus.setStatus("current")
_DDhcpRPoolRelaySourceTable_Object = MibTable
dDhcpRPoolRelaySourceTable = _DDhcpRPoolRelaySourceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourceTable.setStatus("current")
_DDhcpRPoolRelaySourceEntry_Object = MibTableRow
dDhcpRPoolRelaySourceEntry = _DDhcpRPoolRelaySourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3, 1)
)
dDhcpRPoolRelaySourceEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelaySourcePoolName"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelaySourceSubnet"),
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelaySourceSubnetMask"),
)
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourceEntry.setStatus("current")
_DDhcpRPoolRelaySourcePoolName_Type = DisplayString
_DDhcpRPoolRelaySourcePoolName_Object = MibTableColumn
dDhcpRPoolRelaySourcePoolName = _DDhcpRPoolRelaySourcePoolName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3, 1, 1),
    _DDhcpRPoolRelaySourcePoolName_Type()
)
dDhcpRPoolRelaySourcePoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourcePoolName.setStatus("current")
_DDhcpRPoolRelaySourceSubnet_Type = IpAddress
_DDhcpRPoolRelaySourceSubnet_Object = MibTableColumn
dDhcpRPoolRelaySourceSubnet = _DDhcpRPoolRelaySourceSubnet_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3, 1, 2),
    _DDhcpRPoolRelaySourceSubnet_Type()
)
dDhcpRPoolRelaySourceSubnet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourceSubnet.setStatus("current")
_DDhcpRPoolRelaySourceSubnetMask_Type = IpAddress
_DDhcpRPoolRelaySourceSubnetMask_Object = MibTableColumn
dDhcpRPoolRelaySourceSubnetMask = _DDhcpRPoolRelaySourceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3, 1, 3),
    _DDhcpRPoolRelaySourceSubnetMask_Type()
)
dDhcpRPoolRelaySourceSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourceSubnetMask.setStatus("current")
_DDhcpRPoolRelaySourceRowStatus_Type = RowStatus
_DDhcpRPoolRelaySourceRowStatus_Object = MibTableColumn
dDhcpRPoolRelaySourceRowStatus = _DDhcpRPoolRelaySourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 2, 3, 1, 99),
    _DDhcpRPoolRelaySourceRowStatus_Type()
)
dDhcpRPoolRelaySourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRPoolRelaySourceRowStatus.setStatus("current")
_DDhcpRelayIfObjects_ObjectIdentity = ObjectIdentity
dDhcpRelayIfObjects = _DDhcpRelayIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3)
)
_DDhcpRIfIgnoreBootpTable_Object = MibTable
dDhcpRIfIgnoreBootpTable = _DDhcpRIfIgnoreBootpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dDhcpRIfIgnoreBootpTable.setStatus("current")
_DDhcpRIfIgnoreBootpEntry_Object = MibTableRow
dDhcpRIfIgnoreBootpEntry = _DDhcpRIfIgnoreBootpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 1, 1)
)
dDhcpRIfIgnoreBootpEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfIgnoreBootpIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRIfIgnoreBootpEntry.setStatus("current")
_DDhcpRIfIgnoreBootpIfIndex_Type = InterfaceIndex
_DDhcpRIfIgnoreBootpIfIndex_Object = MibTableColumn
dDhcpRIfIgnoreBootpIfIndex = _DDhcpRIfIgnoreBootpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 1, 1, 1),
    _DDhcpRIfIgnoreBootpIfIndex_Type()
)
dDhcpRIfIgnoreBootpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRIfIgnoreBootpIfIndex.setStatus("current")
_DDhcpRIfIgnoreBootpEnabled_Type = TruthValue
_DDhcpRIfIgnoreBootpEnabled_Object = MibTableColumn
dDhcpRIfIgnoreBootpEnabled = _DDhcpRIfIgnoreBootpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 1, 1, 2),
    _DDhcpRIfIgnoreBootpEnabled_Type()
)
dDhcpRIfIgnoreBootpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRIfIgnoreBootpEnabled.setStatus("current")
_DDhcpRIfAgentInfoChkTable_Object = MibTable
dDhcpRIfAgentInfoChkTable = _DDhcpRIfAgentInfoChkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoChkTable.setStatus("current")
_DDhcpRIfAgentInfoChkEntry_Object = MibTableRow
dDhcpRIfAgentInfoChkEntry = _DDhcpRIfAgentInfoChkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 2, 1)
)
dDhcpRIfAgentInfoChkEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoChkIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoChkEntry.setStatus("current")
_DDhcpRIfAgentInfoChkIfIndex_Type = InterfaceIndex
_DDhcpRIfAgentInfoChkIfIndex_Object = MibTableColumn
dDhcpRIfAgentInfoChkIfIndex = _DDhcpRIfAgentInfoChkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 2, 1, 1),
    _DDhcpRIfAgentInfoChkIfIndex_Type()
)
dDhcpRIfAgentInfoChkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoChkIfIndex.setStatus("current")


class _DDhcpRIfAgentInfoChkState_Type(Integer32):
    """Custom type dDhcpRIfAgentInfoChkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("none", 3))
    )


_DDhcpRIfAgentInfoChkState_Type.__name__ = "Integer32"
_DDhcpRIfAgentInfoChkState_Object = MibTableColumn
dDhcpRIfAgentInfoChkState = _DDhcpRIfAgentInfoChkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 2, 1, 2),
    _DDhcpRIfAgentInfoChkState_Type()
)
dDhcpRIfAgentInfoChkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoChkState.setStatus("current")
_DDhcpRIfAgentInfoInsertTable_Object = MibTable
dDhcpRIfAgentInfoInsertTable = _DDhcpRIfAgentInfoInsertTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoInsertTable.setStatus("current")
_DDhcpRIfAgentInfoInsertEntry_Object = MibTableRow
dDhcpRIfAgentInfoInsertEntry = _DDhcpRIfAgentInfoInsertEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 3, 1)
)
dDhcpRIfAgentInfoInsertEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoInsertIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoInsertEntry.setStatus("current")
_DDhcpRIfAgentInfoInsertIfIndex_Type = InterfaceIndex
_DDhcpRIfAgentInfoInsertIfIndex_Object = MibTableColumn
dDhcpRIfAgentInfoInsertIfIndex = _DDhcpRIfAgentInfoInsertIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 3, 1, 1),
    _DDhcpRIfAgentInfoInsertIfIndex_Type()
)
dDhcpRIfAgentInfoInsertIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoInsertIfIndex.setStatus("current")


class _DDhcpRIfAgentInfoInsertState_Type(Integer32):
    """Custom type dDhcpRIfAgentInfoInsertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("none", 3))
    )


_DDhcpRIfAgentInfoInsertState_Type.__name__ = "Integer32"
_DDhcpRIfAgentInfoInsertState_Object = MibTableColumn
dDhcpRIfAgentInfoInsertState = _DDhcpRIfAgentInfoInsertState_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 3, 1, 2),
    _DDhcpRIfAgentInfoInsertState_Type()
)
dDhcpRIfAgentInfoInsertState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoInsertState.setStatus("current")
_DDhcpRIfAgentInfoPolicyTable_Object = MibTable
dDhcpRIfAgentInfoPolicyTable = _DDhcpRIfAgentInfoPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoPolicyTable.setStatus("current")
_DDhcpRIfAgentInfoPolicyEntry_Object = MibTableRow
dDhcpRIfAgentInfoPolicyEntry = _DDhcpRIfAgentInfoPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 4, 1)
)
dDhcpRIfAgentInfoPolicyEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoPolicyEntry.setStatus("current")
_DDhcpRIfAgentInfoPolicyIfIndex_Type = InterfaceIndex
_DDhcpRIfAgentInfoPolicyIfIndex_Object = MibTableColumn
dDhcpRIfAgentInfoPolicyIfIndex = _DDhcpRIfAgentInfoPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 4, 1, 1),
    _DDhcpRIfAgentInfoPolicyIfIndex_Type()
)
dDhcpRIfAgentInfoPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoPolicyIfIndex.setStatus("current")


class _DDhcpRIfAgentInfoPolicyAction_Type(Integer32):
    """Custom type dDhcpRIfAgentInfoPolicyAction based on Integer32"""
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
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3),
          ("none", 4))
    )


_DDhcpRIfAgentInfoPolicyAction_Type.__name__ = "Integer32"
_DDhcpRIfAgentInfoPolicyAction_Object = MibTableColumn
dDhcpRIfAgentInfoPolicyAction = _DDhcpRIfAgentInfoPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 4, 1, 2),
    _DDhcpRIfAgentInfoPolicyAction_Type()
)
dDhcpRIfAgentInfoPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoPolicyAction.setStatus("current")
_DDhcpRIfAgentInfoTrustTable_Object = MibTable
dDhcpRIfAgentInfoTrustTable = _DDhcpRIfAgentInfoTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoTrustTable.setStatus("current")
_DDhcpRIfAgentInfoTrustEntry_Object = MibTableRow
dDhcpRIfAgentInfoTrustEntry = _DDhcpRIfAgentInfoTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 5, 1)
)
dDhcpRIfAgentInfoTrustEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoTrustIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoTrustEntry.setStatus("current")
_DDhcpRIfAgentInfoTrustIfIndex_Type = InterfaceIndex
_DDhcpRIfAgentInfoTrustIfIndex_Object = MibTableColumn
dDhcpRIfAgentInfoTrustIfIndex = _DDhcpRIfAgentInfoTrustIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 5, 1, 1),
    _DDhcpRIfAgentInfoTrustIfIndex_Type()
)
dDhcpRIfAgentInfoTrustIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoTrustIfIndex.setStatus("current")
_DDhcpRIfAgentInfoTrustEnabled_Type = TruthValue
_DDhcpRIfAgentInfoTrustEnabled_Object = MibTableColumn
dDhcpRIfAgentInfoTrustEnabled = _DDhcpRIfAgentInfoTrustEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 3, 5, 1, 2),
    _DDhcpRIfAgentInfoTrustEnabled_Type()
)
dDhcpRIfAgentInfoTrustEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRIfAgentInfoTrustEnabled.setStatus("current")
_DDhcpRelayPortIfOption82Objects_ObjectIdentity = ObjectIdentity
dDhcpRelayPortIfOption82Objects = _DDhcpRelayPortIfOption82Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4)
)
_DDhcpRPortIfOp82RemIdTable_Object = MibTable
dDhcpRPortIfOp82RemIdTable = _DDhcpRPortIfOp82RemIdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82RemIdTable.setStatus("current")
_DDhcpRPortIfOp82RemIdEntry_Object = MibTableRow
dDhcpRPortIfOp82RemIdEntry = _DDhcpRPortIfOp82RemIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 1, 1)
)
dDhcpRPortIfOp82RemIdEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPortIfOp82RemIdIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82RemIdEntry.setStatus("current")
_DDhcpRPortIfOp82RemIdIfIndex_Type = InterfaceIndex
_DDhcpRPortIfOp82RemIdIfIndex_Object = MibTableColumn
dDhcpRPortIfOp82RemIdIfIndex = _DDhcpRPortIfOp82RemIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 1, 1, 1),
    _DDhcpRPortIfOp82RemIdIfIndex_Type()
)
dDhcpRPortIfOp82RemIdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82RemIdIfIndex.setStatus("current")


class _DDhcpRPortIfOp82RemIdVendor3Cfg_Type(DisplayString):
    """Custom type dDhcpRPortIfOp82RemIdVendor3Cfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpRPortIfOp82RemIdVendor3Cfg_Type.__name__ = "DisplayString"
_DDhcpRPortIfOp82RemIdVendor3Cfg_Object = MibTableColumn
dDhcpRPortIfOp82RemIdVendor3Cfg = _DDhcpRPortIfOp82RemIdVendor3Cfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 1, 1, 2),
    _DDhcpRPortIfOp82RemIdVendor3Cfg_Type()
)
dDhcpRPortIfOp82RemIdVendor3Cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82RemIdVendor3Cfg.setStatus("current")
_DDhcpRPortIfOp82CirIdTable_Object = MibTable
dDhcpRPortIfOp82CirIdTable = _DDhcpRPortIfOp82CirIdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82CirIdTable.setStatus("current")
_DDhcpRPortIfOp82CirIdEntry_Object = MibTableRow
dDhcpRPortIfOp82CirIdEntry = _DDhcpRPortIfOp82CirIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 2, 1)
)
dDhcpRPortIfOp82CirIdEntry.setIndexNames(
    (0, "DLINKSW-DHCP-RELAY-MIB", "dDhcpRPortIfOp82CirIdIfIndex"),
)
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82CirIdEntry.setStatus("current")
_DDhcpRPortIfOp82CirIdIfIndex_Type = InterfaceIndex
_DDhcpRPortIfOp82CirIdIfIndex_Object = MibTableColumn
dDhcpRPortIfOp82CirIdIfIndex = _DDhcpRPortIfOp82CirIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 2, 1, 1),
    _DDhcpRPortIfOp82CirIdIfIndex_Type()
)
dDhcpRPortIfOp82CirIdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82CirIdIfIndex.setStatus("current")


class _DDhcpRPortIfOp82CirIdVendor3Cfg_Type(DisplayString):
    """Custom type dDhcpRPortIfOp82CirIdVendor3Cfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DDhcpRPortIfOp82CirIdVendor3Cfg_Type.__name__ = "DisplayString"
_DDhcpRPortIfOp82CirIdVendor3Cfg_Object = MibTableColumn
dDhcpRPortIfOp82CirIdVendor3Cfg = _DDhcpRPortIfOp82CirIdVendor3Cfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 4, 2, 1, 2),
    _DDhcpRPortIfOp82CirIdVendor3Cfg_Type()
)
dDhcpRPortIfOp82CirIdVendor3Cfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRPortIfOp82CirIdVendor3Cfg.setStatus("current")
_DDhcpRelayVlanObjects_ObjectIdentity = ObjectIdentity
dDhcpRelayVlanObjects = _DDhcpRelayVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 5)
)
_DDhcpRVlanLocalRelayCrlFirst2K_Type = Dlink2kVlanList
_DDhcpRVlanLocalRelayCrlFirst2K_Object = MibScalar
dDhcpRVlanLocalRelayCrlFirst2K = _DDhcpRVlanLocalRelayCrlFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 5, 1),
    _DDhcpRVlanLocalRelayCrlFirst2K_Type()
)
dDhcpRVlanLocalRelayCrlFirst2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRVlanLocalRelayCrlFirst2K.setStatus("current")
_DDhcpRVlanLocalRelayCrlSecond2K_Type = Dlink2kVlanList
_DDhcpRVlanLocalRelayCrlSecond2K_Object = MibScalar
dDhcpRVlanLocalRelayCrlSecond2K = _DDhcpRVlanLocalRelayCrlSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 1, 5, 2),
    _DDhcpRVlanLocalRelayCrlSecond2K_Type()
)
dDhcpRVlanLocalRelayCrlSecond2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dDhcpRVlanLocalRelayCrlSecond2K.setStatus("current")
_DDhcpRelayMIBConformance_ObjectIdentity = ObjectIdentity
dDhcpRelayMIBConformance = _DDhcpRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2)
)
_DDhcpRelayCompliances_ObjectIdentity = ObjectIdentity
dDhcpRelayCompliances = _DDhcpRelayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 1)
)
_DDhcpRelayGroups_ObjectIdentity = ObjectIdentity
dDhcpRelayGroups = _DDhcpRelayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2)
)

# Managed Objects groups

dDhcpRGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2, 1)
)
dDhcpRGblCfgGroup.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpRelayAgentInfoCheckEnabled"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRelayAgentInfoInsertEnabled"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRelayAgentInfoPolicy"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRelayInfoTrustAll"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRelaySmartRelay"))
)
if mibBuilder.loadTexts:
    dDhcpRGblCfgGroup.setStatus("current")

dDhcpRPoolCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2, 2)
)
dDhcpRPoolCfgGroup.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoClRelayTargetRowStatus"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelayDestRowStatus"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolRelaySourceRowStatus"))
)
if mibBuilder.loadTexts:
    dDhcpRPoolCfgGroup.setStatus("current")

dDhcpRInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2, 3)
)
dDhcpRInterfaceGroup.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfIgnoreBootpEnabled"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoChkState"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoInsertState"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoPolicyAction"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRIfAgentInfoTrustEnabled"))
)
if mibBuilder.loadTexts:
    dDhcpRInterfaceGroup.setStatus("current")

dDhcpROp82SuboptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2, 4)
)
dDhcpROp82SuboptionGroup.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpROption82RemoteIdType"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpROption82RemoteIdUserDef"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpROption82CircuitIdType"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpROption82CircuitIdUserDef"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPortIfOp82RemIdVendor3Cfg"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPortIfOp82CirIdVendor3Cfg"))
)
if mibBuilder.loadTexts:
    dDhcpROp82SuboptionGroup.setStatus("current")

dDhcpRVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 2, 5)
)
dDhcpRVlanCfgGroup.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpRVlanLocalRelayCrlFirst2K"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRVlanLocalRelayCrlSecond2K"))
)
if mibBuilder.loadTexts:
    dDhcpRVlanCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 23, 2, 1, 1)
)
dDhcpRelayCompliance.setObjects(
      *(("DLINKSW-DHCP-RELAY-MIB", "dDhcpRGblCfgGroup"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRPoolCfgGroup"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRInterfaceGroup"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpROp82SuboptionGroup"),
        ("DLINKSW-DHCP-RELAY-MIB", "dDhcpRVlanCfgGroup"))
)
if mibBuilder.loadTexts:
    dDhcpRelayCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-DHCP-RELAY-MIB",
    **{"dlinkSwDhcpRelayMIB": dlinkSwDhcpRelayMIB,
       "dDhcpRelayMIBNotifications": dDhcpRelayMIBNotifications,
       "dDhcpRelayMIBObjects": dDhcpRelayMIBObjects,
       "dDhcpRelayGeneral": dDhcpRelayGeneral,
       "dDhcpRelayAgentInfoCheckEnabled": dDhcpRelayAgentInfoCheckEnabled,
       "dDhcpRelayAgentInfoInsertEnabled": dDhcpRelayAgentInfoInsertEnabled,
       "dDhcpRelayAgentInfoPolicy": dDhcpRelayAgentInfoPolicy,
       "dDhcpRelayInfoTrustAll": dDhcpRelayInfoTrustAll,
       "dDhcpRelaySmartRelay": dDhcpRelaySmartRelay,
       "dDhcpROption82RemoteIdType": dDhcpROption82RemoteIdType,
       "dDhcpROption82RemoteIdUserDef": dDhcpROption82RemoteIdUserDef,
       "dDhcpROption82CircuitIdType": dDhcpROption82CircuitIdType,
       "dDhcpROption82CircuitIdUserDef": dDhcpROption82CircuitIdUserDef,
       "dDhcpRPoolObjects": dDhcpRPoolObjects,
       "dDhcpRPoolClassRelayTargetTable": dDhcpRPoolClassRelayTargetTable,
       "dDhcpRPoolClassRelayTargetEntry": dDhcpRPoolClassRelayTargetEntry,
       "dDhcpRPoClRelayTargetPoolName": dDhcpRPoClRelayTargetPoolName,
       "dDhcpRPoClRelayTargetClassName": dDhcpRPoClRelayTargetClassName,
       "dDhcpRPoClRelayTargetVrfName": dDhcpRPoClRelayTargetVrfName,
       "dDhcpRPoClRelayTargetAddr": dDhcpRPoClRelayTargetAddr,
       "dDhcpRPoClRelayTargetRowStatus": dDhcpRPoClRelayTargetRowStatus,
       "dDhcpRPoolRelayDestTable": dDhcpRPoolRelayDestTable,
       "dDhcpRPoolRelayDestEntry": dDhcpRPoolRelayDestEntry,
       "dDhcpRPoolRelayDestPoolName": dDhcpRPoolRelayDestPoolName,
       "dDhcpRPoolRelayDestVrfName": dDhcpRPoolRelayDestVrfName,
       "dDhcpRPoolRelayDestAddr": dDhcpRPoolRelayDestAddr,
       "dDhcpRPoolRelayDestRowStatus": dDhcpRPoolRelayDestRowStatus,
       "dDhcpRPoolRelaySourceTable": dDhcpRPoolRelaySourceTable,
       "dDhcpRPoolRelaySourceEntry": dDhcpRPoolRelaySourceEntry,
       "dDhcpRPoolRelaySourcePoolName": dDhcpRPoolRelaySourcePoolName,
       "dDhcpRPoolRelaySourceSubnet": dDhcpRPoolRelaySourceSubnet,
       "dDhcpRPoolRelaySourceSubnetMask": dDhcpRPoolRelaySourceSubnetMask,
       "dDhcpRPoolRelaySourceRowStatus": dDhcpRPoolRelaySourceRowStatus,
       "dDhcpRelayIfObjects": dDhcpRelayIfObjects,
       "dDhcpRIfIgnoreBootpTable": dDhcpRIfIgnoreBootpTable,
       "dDhcpRIfIgnoreBootpEntry": dDhcpRIfIgnoreBootpEntry,
       "dDhcpRIfIgnoreBootpIfIndex": dDhcpRIfIgnoreBootpIfIndex,
       "dDhcpRIfIgnoreBootpEnabled": dDhcpRIfIgnoreBootpEnabled,
       "dDhcpRIfAgentInfoChkTable": dDhcpRIfAgentInfoChkTable,
       "dDhcpRIfAgentInfoChkEntry": dDhcpRIfAgentInfoChkEntry,
       "dDhcpRIfAgentInfoChkIfIndex": dDhcpRIfAgentInfoChkIfIndex,
       "dDhcpRIfAgentInfoChkState": dDhcpRIfAgentInfoChkState,
       "dDhcpRIfAgentInfoInsertTable": dDhcpRIfAgentInfoInsertTable,
       "dDhcpRIfAgentInfoInsertEntry": dDhcpRIfAgentInfoInsertEntry,
       "dDhcpRIfAgentInfoInsertIfIndex": dDhcpRIfAgentInfoInsertIfIndex,
       "dDhcpRIfAgentInfoInsertState": dDhcpRIfAgentInfoInsertState,
       "dDhcpRIfAgentInfoPolicyTable": dDhcpRIfAgentInfoPolicyTable,
       "dDhcpRIfAgentInfoPolicyEntry": dDhcpRIfAgentInfoPolicyEntry,
       "dDhcpRIfAgentInfoPolicyIfIndex": dDhcpRIfAgentInfoPolicyIfIndex,
       "dDhcpRIfAgentInfoPolicyAction": dDhcpRIfAgentInfoPolicyAction,
       "dDhcpRIfAgentInfoTrustTable": dDhcpRIfAgentInfoTrustTable,
       "dDhcpRIfAgentInfoTrustEntry": dDhcpRIfAgentInfoTrustEntry,
       "dDhcpRIfAgentInfoTrustIfIndex": dDhcpRIfAgentInfoTrustIfIndex,
       "dDhcpRIfAgentInfoTrustEnabled": dDhcpRIfAgentInfoTrustEnabled,
       "dDhcpRelayPortIfOption82Objects": dDhcpRelayPortIfOption82Objects,
       "dDhcpRPortIfOp82RemIdTable": dDhcpRPortIfOp82RemIdTable,
       "dDhcpRPortIfOp82RemIdEntry": dDhcpRPortIfOp82RemIdEntry,
       "dDhcpRPortIfOp82RemIdIfIndex": dDhcpRPortIfOp82RemIdIfIndex,
       "dDhcpRPortIfOp82RemIdVendor3Cfg": dDhcpRPortIfOp82RemIdVendor3Cfg,
       "dDhcpRPortIfOp82CirIdTable": dDhcpRPortIfOp82CirIdTable,
       "dDhcpRPortIfOp82CirIdEntry": dDhcpRPortIfOp82CirIdEntry,
       "dDhcpRPortIfOp82CirIdIfIndex": dDhcpRPortIfOp82CirIdIfIndex,
       "dDhcpRPortIfOp82CirIdVendor3Cfg": dDhcpRPortIfOp82CirIdVendor3Cfg,
       "dDhcpRelayVlanObjects": dDhcpRelayVlanObjects,
       "dDhcpRVlanLocalRelayCrlFirst2K": dDhcpRVlanLocalRelayCrlFirst2K,
       "dDhcpRVlanLocalRelayCrlSecond2K": dDhcpRVlanLocalRelayCrlSecond2K,
       "dDhcpRelayMIBConformance": dDhcpRelayMIBConformance,
       "dDhcpRelayCompliances": dDhcpRelayCompliances,
       "dDhcpRelayCompliance": dDhcpRelayCompliance,
       "dDhcpRelayGroups": dDhcpRelayGroups,
       "dDhcpRGblCfgGroup": dDhcpRGblCfgGroup,
       "dDhcpRPoolCfgGroup": dDhcpRPoolCfgGroup,
       "dDhcpRInterfaceGroup": dDhcpRInterfaceGroup,
       "dDhcpROp82SuboptionGroup": dDhcpROp82SuboptionGroup,
       "dDhcpRVlanCfgGroup": dDhcpRVlanCfgGroup}
)
