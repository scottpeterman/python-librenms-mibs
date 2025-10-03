# SNMP MIB module (CISCO-QOS-POLICY-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-QOS-POLICY-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:13 2025
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

(QosInterfaceQueueType,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "QosInterfaceQueueType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoQosPolicyConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159)
)
if mibBuilder.loadTexts:
    ciscoQosPolicyConfigMIB.setRevisions(
        ("2000-11-02 10:30",
         "2000-02-26 19:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QosPolicySource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2),
          ("cops", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoQosPolicyConfigMIBObjects_ObjectIdentity = ObjectIdentity
ciscoQosPolicyConfigMIBObjects = _CiscoQosPolicyConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1)
)
_QosPolicyGlobalObjects_ObjectIdentity = ObjectIdentity
qosPolicyGlobalObjects = _QosPolicyGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1)
)


class _QosEnabled_Type(TruthValue):
    """Custom type qosEnabled based on TruthValue"""
    defaultValue = 2


_QosEnabled_Type.__name__ = "TruthValue"
_QosEnabled_Object = MibScalar
qosEnabled = _QosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 1),
    _QosEnabled_Type()
)
qosEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEnabled.setStatus("current")


class _QosPrAdminPolicySource_Type(QosPolicySource):
    """Custom type qosPrAdminPolicySource based on QosPolicySource"""
    defaultValue = 2


_QosPrAdminPolicySource_Type.__name__ = "QosPolicySource"
_QosPrAdminPolicySource_Object = MibScalar
qosPrAdminPolicySource = _QosPrAdminPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 2),
    _QosPrAdminPolicySource_Type()
)
qosPrAdminPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPrAdminPolicySource.setStatus("current")
_QosPrOperPolicySource_Type = QosPolicySource
_QosPrOperPolicySource_Object = MibScalar
qosPrOperPolicySource = _QosPrOperPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 3),
    _QosPrOperPolicySource_Type()
)
qosPrOperPolicySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPrOperPolicySource.setStatus("current")


class _QosRsvpAdminPolicySource_Type(QosPolicySource):
    """Custom type qosRsvpAdminPolicySource based on QosPolicySource"""
    defaultValue = 2


_QosRsvpAdminPolicySource_Type.__name__ = "QosPolicySource"
_QosRsvpAdminPolicySource_Object = MibScalar
qosRsvpAdminPolicySource = _QosRsvpAdminPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 4),
    _QosRsvpAdminPolicySource_Type()
)
qosRsvpAdminPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRsvpAdminPolicySource.setStatus("current")
_QosRsvpOperPolicySource_Type = QosPolicySource
_QosRsvpOperPolicySource_Object = MibScalar
qosRsvpOperPolicySource = _QosRsvpOperPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 5),
    _QosRsvpOperPolicySource_Type()
)
qosRsvpOperPolicySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRsvpOperPolicySource.setStatus("current")


class _QosCopsPolicyStatus_Type(Integer32):
    """Custom type qosCopsPolicyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("discard", 2))
    )


_QosCopsPolicyStatus_Type.__name__ = "Integer32"
_QosCopsPolicyStatus_Object = MibScalar
qosCopsPolicyStatus = _QosCopsPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 6),
    _QosCopsPolicyStatus_Type()
)
qosCopsPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCopsPolicyStatus.setStatus("current")
_QosPolicyInterfaceObjects_ObjectIdentity = ObjectIdentity
qosPolicyInterfaceObjects = _QosPolicyInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2)
)
_QosPrIfTable_Object = MibTable
qosPrIfTable = _QosPrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qosPrIfTable.setStatus("current")
_QosPrIfEntry_Object = MibTableRow
qosPrIfEntry = _QosPrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1)
)
qosPrIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qosPrIfEntry.setStatus("current")


class _QosPrIfAdminPolicySource_Type(QosPolicySource):
    """Custom type qosPrIfAdminPolicySource based on QosPolicySource"""
    defaultValue = 3


_QosPrIfAdminPolicySource_Type.__name__ = "QosPolicySource"
_QosPrIfAdminPolicySource_Object = MibTableColumn
qosPrIfAdminPolicySource = _QosPrIfAdminPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 1),
    _QosPrIfAdminPolicySource_Type()
)
qosPrIfAdminPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPrIfAdminPolicySource.setStatus("current")
_QosPrIfOperPolicySource_Type = QosPolicySource
_QosPrIfOperPolicySource_Object = MibTableColumn
qosPrIfOperPolicySource = _QosPrIfOperPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 2),
    _QosPrIfOperPolicySource_Type()
)
qosPrIfOperPolicySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPrIfOperPolicySource.setStatus("current")
_QosIfCapabilityTable_Object = MibTable
qosIfCapabilityTable = _QosIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qosIfCapabilityTable.setStatus("current")
_QosIfCapabilityEntry_Object = MibTableRow
qosIfCapabilityEntry = _QosIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1)
)
qosIfCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfDirection"),
    (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfQType"),
)
if mibBuilder.loadTexts:
    qosIfCapabilityEntry.setStatus("current")


class _QosIfDirection_Type(Integer32):
    """Custom type qosIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_QosIfDirection_Type.__name__ = "Integer32"
_QosIfDirection_Object = MibTableColumn
qosIfDirection = _QosIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 1),
    _QosIfDirection_Type()
)
qosIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfDirection.setStatus("current")
_QosIfQType_Type = QosInterfaceQueueType
_QosIfQType_Object = MibTableColumn
qosIfQType = _QosIfQType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 2),
    _QosIfQType_Type()
)
qosIfQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIfQType.setStatus("current")


class _QosIfCapabilities_Type(Bits):
    """Custom type qosIfCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("inputL2Classification", 1),
          ("inputIpClassification", 2),
          ("outputL2Classification", 3),
          ("outputIpClassification", 4),
          ("inputUflowPolicing", 5),
          ("inputAggregatePolicing", 6),
          ("outputUflowPolicing", 7),
          ("outputAggregatePolicing", 8),
          ("policeByMarkingDown", 9),
          ("policeByDropping", 10),
          ("fifo", 11),
          ("wrr", 12),
          ("wfq", 13),
          ("cq", 14),
          ("pq", 15),
          ("cbwfq", 16),
          ("tailDrop", 17),
          ("wred", 18),
          ("inputPortClassification", 19),
          ("outputPortClassification", 20),
          ("inputUflowShaping", 21),
          ("inputAggregateShaping", 22),
          ("outputUflowShaping", 23),
          ("outputAggregateShaping", 24),
          ("pqWrr", 25),
          ("pqCbwfq", 26))
    )

_QosIfCapabilities_Type.__name__ = "Bits"
_QosIfCapabilities_Object = MibTableColumn
qosIfCapabilities = _QosIfCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 3),
    _QosIfCapabilities_Type()
)
qosIfCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfCapabilities.setStatus("current")
_CiscoQosPolicyMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoQosPolicyMIBNotifications = _CiscoQosPolicyMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 2)
)
_CiscoQosPolicyConfigMIBConformance_ObjectIdentity = ObjectIdentity
ciscoQosPolicyConfigMIBConformance = _CiscoQosPolicyConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3)
)
_CiscoQosPolicyConfigMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoQosPolicyConfigMIBCompliances = _CiscoQosPolicyConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1)
)
_CiscoQosPolicyConfigMIBGroups_ObjectIdentity = ObjectIdentity
ciscoQosPolicyConfigMIBGroups = _CiscoQosPolicyConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2)
)

# Managed Objects groups

qosGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 1)
)
qosGlobalGroup.setObjects(
    ("CISCO-QOS-POLICY-CONFIG-MIB", "qosEnabled")
)
if mibBuilder.loadTexts:
    qosGlobalGroup.setStatus("current")

qosPrGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 2)
)
qosPrGlobalGroup.setObjects(
      *(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrAdminPolicySource"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrOperPolicySource"))
)
if mibBuilder.loadTexts:
    qosPrGlobalGroup.setStatus("current")

qosRsvpGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 3)
)
qosRsvpGlobalGroup.setObjects(
      *(("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpAdminPolicySource"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpOperPolicySource"))
)
if mibBuilder.loadTexts:
    qosRsvpGlobalGroup.setStatus("current")

qosPrInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 4)
)
qosPrInterfaceGroup.setObjects(
      *(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfAdminPolicySource"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfOperPolicySource"))
)
if mibBuilder.loadTexts:
    qosPrInterfaceGroup.setStatus("current")

qosInterfaceCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 5)
)
qosInterfaceCapabilityGroup.setObjects(
    ("CISCO-QOS-POLICY-CONFIG-MIB", "qosIfCapabilities")
)
if mibBuilder.loadTexts:
    qosInterfaceCapabilityGroup.setStatus("current")

qosCopsPolicyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 6)
)
qosCopsPolicyStatusGroup.setObjects(
    ("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatus")
)
if mibBuilder.loadTexts:
    qosCopsPolicyStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoQosPolicyConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1, 1)
)
ciscoQosPolicyConfigMIBCompliance.setObjects(
      *(("CISCO-QOS-POLICY-CONFIG-MIB", "qosGlobalGroup"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrGlobalGroup"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpGlobalGroup"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrInterfaceGroup"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosInterfaceCapabilityGroup"),
        ("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoQosPolicyConfigMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QOS-POLICY-CONFIG-MIB",
    **{"QosPolicySource": QosPolicySource,
       "ciscoQosPolicyConfigMIB": ciscoQosPolicyConfigMIB,
       "ciscoQosPolicyConfigMIBObjects": ciscoQosPolicyConfigMIBObjects,
       "qosPolicyGlobalObjects": qosPolicyGlobalObjects,
       "qosEnabled": qosEnabled,
       "qosPrAdminPolicySource": qosPrAdminPolicySource,
       "qosPrOperPolicySource": qosPrOperPolicySource,
       "qosRsvpAdminPolicySource": qosRsvpAdminPolicySource,
       "qosRsvpOperPolicySource": qosRsvpOperPolicySource,
       "qosCopsPolicyStatus": qosCopsPolicyStatus,
       "qosPolicyInterfaceObjects": qosPolicyInterfaceObjects,
       "qosPrIfTable": qosPrIfTable,
       "qosPrIfEntry": qosPrIfEntry,
       "qosPrIfAdminPolicySource": qosPrIfAdminPolicySource,
       "qosPrIfOperPolicySource": qosPrIfOperPolicySource,
       "qosIfCapabilityTable": qosIfCapabilityTable,
       "qosIfCapabilityEntry": qosIfCapabilityEntry,
       "qosIfDirection": qosIfDirection,
       "qosIfQType": qosIfQType,
       "qosIfCapabilities": qosIfCapabilities,
       "ciscoQosPolicyMIBNotifications": ciscoQosPolicyMIBNotifications,
       "ciscoQosPolicyConfigMIBConformance": ciscoQosPolicyConfigMIBConformance,
       "ciscoQosPolicyConfigMIBCompliances": ciscoQosPolicyConfigMIBCompliances,
       "ciscoQosPolicyConfigMIBCompliance": ciscoQosPolicyConfigMIBCompliance,
       "ciscoQosPolicyConfigMIBGroups": ciscoQosPolicyConfigMIBGroups,
       "qosGlobalGroup": qosGlobalGroup,
       "qosPrGlobalGroup": qosPrGlobalGroup,
       "qosRsvpGlobalGroup": qosRsvpGlobalGroup,
       "qosPrInterfaceGroup": qosPrInterfaceGroup,
       "qosInterfaceCapabilityGroup": qosInterfaceCapabilityGroup,
       "qosCopsPolicyStatusGroup": qosCopsPolicyStatusGroup}
)
