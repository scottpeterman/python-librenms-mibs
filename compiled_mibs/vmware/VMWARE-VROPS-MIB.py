# SNMP MIB module (VMWARE-VROPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-VROPS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:40 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwVrops,) = mibBuilder.importSymbols(
    "VMWARE-PRODUCTS-MIB",
    "vmwVrops")

(VmwLongDisplayString,) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwLongDisplayString")


# MODULE-IDENTITY

vmwVropsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1)
)
if mibBuilder.loadTexts:
    vmwVropsMIB.setRevisions(
        ("2018-06-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwAlertTrap_ObjectIdentity = ObjectIdentity
vmwAlertTrap = _VmwAlertTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 0)
)
if mibBuilder.loadTexts:
    vmwAlertTrap.setStatus("current")
_VmwGenericAlertData_ObjectIdentity = ObjectIdentity
vmwGenericAlertData = _VmwGenericAlertData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2)
)
if mibBuilder.loadTexts:
    vmwGenericAlertData.setStatus("current")
_VmwAlertAliveServerName_Type = VmwLongDisplayString
_VmwAlertAliveServerName_Object = MibScalar
vmwAlertAliveServerName = _VmwAlertAliveServerName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 1),
    _VmwAlertAliveServerName_Type()
)
vmwAlertAliveServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertAliveServerName.setStatus("current")
_VmwAlertEntityName_Type = VmwLongDisplayString
_VmwAlertEntityName_Object = MibScalar
vmwAlertEntityName = _VmwAlertEntityName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 2),
    _VmwAlertEntityName_Type()
)
vmwAlertEntityName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertEntityName.setStatus("current")
_VmwAlertEntityType_Type = VmwLongDisplayString
_VmwAlertEntityType_Object = MibScalar
vmwAlertEntityType = _VmwAlertEntityType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 3),
    _VmwAlertEntityType_Type()
)
vmwAlertEntityType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertEntityType.setStatus("current")
_VmwAlertTimestamp_Type = VmwLongDisplayString
_VmwAlertTimestamp_Object = MibScalar
vmwAlertTimestamp = _VmwAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 4),
    _VmwAlertTimestamp_Type()
)
vmwAlertTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertTimestamp.setStatus("current")
_VmwAlertCriticality_Type = VmwLongDisplayString
_VmwAlertCriticality_Object = MibScalar
vmwAlertCriticality = _VmwAlertCriticality_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 5),
    _VmwAlertCriticality_Type()
)
vmwAlertCriticality.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertCriticality.setStatus("current")
_VmwAlertRootCause_Type = VmwLongDisplayString
_VmwAlertRootCause_Object = MibScalar
vmwAlertRootCause = _VmwAlertRootCause_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 6),
    _VmwAlertRootCause_Type()
)
vmwAlertRootCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertRootCause.setStatus("current")
_VmwAlertURL_Type = VmwLongDisplayString
_VmwAlertURL_Object = MibScalar
vmwAlertURL = _VmwAlertURL_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 7),
    _VmwAlertURL_Type()
)
vmwAlertURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertURL.setStatus("current")
_VmwAlertID_Type = VmwLongDisplayString
_VmwAlertID_Object = MibScalar
vmwAlertID = _VmwAlertID_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 8),
    _VmwAlertID_Type()
)
vmwAlertID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertID.setStatus("current")
_VmwAlertMessage_Type = VmwLongDisplayString
_VmwAlertMessage_Object = MibScalar
vmwAlertMessage = _VmwAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 9),
    _VmwAlertMessage_Type()
)
vmwAlertMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertMessage.setStatus("current")
_VmwAlertType_Type = VmwLongDisplayString
_VmwAlertType_Object = MibScalar
vmwAlertType = _VmwAlertType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 10),
    _VmwAlertType_Type()
)
vmwAlertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertType.setStatus("current")
_VmwAlertSubtype_Type = VmwLongDisplayString
_VmwAlertSubtype_Object = MibScalar
vmwAlertSubtype = _VmwAlertSubtype_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 11),
    _VmwAlertSubtype_Type()
)
vmwAlertSubtype.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertSubtype.setStatus("current")
_VmwAlertHealth_Type = SnmpAdminString
_VmwAlertHealth_Object = MibScalar
vmwAlertHealth = _VmwAlertHealth_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 12),
    _VmwAlertHealth_Type()
)
vmwAlertHealth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertHealth.setStatus("current")
_VmwAlertRisk_Type = SnmpAdminString
_VmwAlertRisk_Object = MibScalar
vmwAlertRisk = _VmwAlertRisk_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 13),
    _VmwAlertRisk_Type()
)
vmwAlertRisk.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertRisk.setStatus("current")
_VmwAlertEfficiency_Type = SnmpAdminString
_VmwAlertEfficiency_Object = MibScalar
vmwAlertEfficiency = _VmwAlertEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 14),
    _VmwAlertEfficiency_Type()
)
vmwAlertEfficiency.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertEfficiency.setStatus("current")
_VmwAlertMetricName_Type = SnmpAdminString
_VmwAlertMetricName_Object = MibScalar
vmwAlertMetricName = _VmwAlertMetricName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 15),
    _VmwAlertMetricName_Type()
)
vmwAlertMetricName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertMetricName.setStatus("current")
_VmwAlertResourceKind_Type = SnmpAdminString
_VmwAlertResourceKind_Object = MibScalar
vmwAlertResourceKind = _VmwAlertResourceKind_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 16),
    _VmwAlertResourceKind_Type()
)
vmwAlertResourceKind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertResourceKind.setStatus("current")
_VmwAlertDefinitionName_Type = SnmpAdminString
_VmwAlertDefinitionName_Object = MibScalar
vmwAlertDefinitionName = _VmwAlertDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 17),
    _VmwAlertDefinitionName_Type()
)
vmwAlertDefinitionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertDefinitionName.setStatus("current")
_VmwAlertDefinitionDesc_Type = SnmpAdminString
_VmwAlertDefinitionDesc_Object = MibScalar
vmwAlertDefinitionDesc = _VmwAlertDefinitionDesc_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 18),
    _VmwAlertDefinitionDesc_Type()
)
vmwAlertDefinitionDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertDefinitionDesc.setStatus("current")
_VmwAlertImpact_Type = SnmpAdminString
_VmwAlertImpact_Object = MibScalar
vmwAlertImpact = _VmwAlertImpact_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 19),
    _VmwAlertImpact_Type()
)
vmwAlertImpact.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertImpact.setStatus("current")
_VmwAlertNotificationRules_Type = VmwLongDisplayString
_VmwAlertNotificationRules_Object = MibScalar
vmwAlertNotificationRules = _VmwAlertNotificationRules_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 2, 20),
    _VmwAlertNotificationRules_Type()
)
vmwAlertNotificationRules.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwAlertNotificationRules.setStatus("current")
_VmwVROPSMIBConformance_ObjectIdentity = ObjectIdentity
vmwVROPSMIBConformance = _VmwVROPSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99)
)
_VmwVROPSMIBCompliances_ObjectIdentity = ObjectIdentity
vmwVROPSMIBCompliances = _VmwVROPSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99, 1)
)
_VmwVROPSMIBGroups_ObjectIdentity = ObjectIdentity
vmwVROPSMIBGroups = _VmwVROPSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99, 2)
)

# Managed Objects groups

vmwVROPSNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99, 2, 1)
)
vmwVROPSNotificationInfoGroup.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwAlertAliveServerName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityType"),
        ("VMWARE-VROPS-MIB", "vmwAlertTimestamp"),
        ("VMWARE-VROPS-MIB", "vmwAlertCriticality"),
        ("VMWARE-VROPS-MIB", "vmwAlertRootCause"),
        ("VMWARE-VROPS-MIB", "vmwAlertURL"),
        ("VMWARE-VROPS-MIB", "vmwAlertID"),
        ("VMWARE-VROPS-MIB", "vmwAlertMessage"),
        ("VMWARE-VROPS-MIB", "vmwAlertType"),
        ("VMWARE-VROPS-MIB", "vmwAlertSubtype"),
        ("VMWARE-VROPS-MIB", "vmwAlertMetricName"),
        ("VMWARE-VROPS-MIB", "vmwAlertResourceKind"),
        ("VMWARE-VROPS-MIB", "vmwAlertHealth"),
        ("VMWARE-VROPS-MIB", "vmwAlertRisk"),
        ("VMWARE-VROPS-MIB", "vmwAlertEfficiency"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionName"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionDesc"),
        ("VMWARE-VROPS-MIB", "vmwAlertImpact"),
        ("VMWARE-VROPS-MIB", "vmwAlertNotificationRules"))
)
if mibBuilder.loadTexts:
    vmwVROPSNotificationInfoGroup.setStatus("current")


# Notification objects

vmwTrapProblemActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 0, 46)
)
vmwTrapProblemActive.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwAlertAliveServerName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityType"),
        ("VMWARE-VROPS-MIB", "vmwAlertTimestamp"),
        ("VMWARE-VROPS-MIB", "vmwAlertCriticality"),
        ("VMWARE-VROPS-MIB", "vmwAlertRootCause"),
        ("VMWARE-VROPS-MIB", "vmwAlertURL"),
        ("VMWARE-VROPS-MIB", "vmwAlertID"),
        ("VMWARE-VROPS-MIB", "vmwAlertMessage"),
        ("VMWARE-VROPS-MIB", "vmwAlertType"),
        ("VMWARE-VROPS-MIB", "vmwAlertSubtype"),
        ("VMWARE-VROPS-MIB", "vmwAlertHealth"),
        ("VMWARE-VROPS-MIB", "vmwAlertRisk"),
        ("VMWARE-VROPS-MIB", "vmwAlertEfficiency"),
        ("VMWARE-VROPS-MIB", "vmwAlertMetricName"),
        ("VMWARE-VROPS-MIB", "vmwAlertResourceKind"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionName"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionDesc"),
        ("VMWARE-VROPS-MIB", "vmwAlertImpact"),
        ("VMWARE-VROPS-MIB", "vmwAlertNotificationRules"))
)
if mibBuilder.loadTexts:
    vmwTrapProblemActive.setStatus(
        "current"
    )

vmwTrapProblemClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 0, 47)
)
vmwTrapProblemClear.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwAlertAliveServerName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityType"),
        ("VMWARE-VROPS-MIB", "vmwAlertTimestamp"),
        ("VMWARE-VROPS-MIB", "vmwAlertCriticality"),
        ("VMWARE-VROPS-MIB", "vmwAlertRootCause"),
        ("VMWARE-VROPS-MIB", "vmwAlertURL"),
        ("VMWARE-VROPS-MIB", "vmwAlertID"),
        ("VMWARE-VROPS-MIB", "vmwAlertMessage"),
        ("VMWARE-VROPS-MIB", "vmwAlertType"),
        ("VMWARE-VROPS-MIB", "vmwAlertSubtype"),
        ("VMWARE-VROPS-MIB", "vmwAlertHealth"),
        ("VMWARE-VROPS-MIB", "vmwAlertRisk"),
        ("VMWARE-VROPS-MIB", "vmwAlertEfficiency"),
        ("VMWARE-VROPS-MIB", "vmwAlertMetricName"),
        ("VMWARE-VROPS-MIB", "vmwAlertResourceKind"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionName"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionDesc"),
        ("VMWARE-VROPS-MIB", "vmwAlertImpact"),
        ("VMWARE-VROPS-MIB", "vmwAlertNotificationRules"))
)
if mibBuilder.loadTexts:
    vmwTrapProblemClear.setStatus(
        "current"
    )

vmwTrapProblemChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 0, 48)
)
vmwTrapProblemChange.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwAlertAliveServerName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityType"),
        ("VMWARE-VROPS-MIB", "vmwAlertTimestamp"),
        ("VMWARE-VROPS-MIB", "vmwAlertCriticality"),
        ("VMWARE-VROPS-MIB", "vmwAlertRootCause"),
        ("VMWARE-VROPS-MIB", "vmwAlertURL"),
        ("VMWARE-VROPS-MIB", "vmwAlertID"),
        ("VMWARE-VROPS-MIB", "vmwAlertMessage"),
        ("VMWARE-VROPS-MIB", "vmwAlertType"),
        ("VMWARE-VROPS-MIB", "vmwAlertSubtype"),
        ("VMWARE-VROPS-MIB", "vmwAlertMetricName"),
        ("VMWARE-VROPS-MIB", "vmwAlertResourceKind"),
        ("VMWARE-VROPS-MIB", "vmwAlertHealth"),
        ("VMWARE-VROPS-MIB", "vmwAlertRisk"),
        ("VMWARE-VROPS-MIB", "vmwAlertEfficiency"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionName"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionDesc"),
        ("VMWARE-VROPS-MIB", "vmwAlertImpact"),
        ("VMWARE-VROPS-MIB", "vmwAlertNotificationRules"))
)
if mibBuilder.loadTexts:
    vmwTrapProblemChange.setStatus(
        "current"
    )

vmwTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 0, 200)
)
vmwTrapTest.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwAlertAliveServerName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityName"),
        ("VMWARE-VROPS-MIB", "vmwAlertEntityType"),
        ("VMWARE-VROPS-MIB", "vmwAlertTimestamp"),
        ("VMWARE-VROPS-MIB", "vmwAlertCriticality"),
        ("VMWARE-VROPS-MIB", "vmwAlertRootCause"),
        ("VMWARE-VROPS-MIB", "vmwAlertURL"),
        ("VMWARE-VROPS-MIB", "vmwAlertID"),
        ("VMWARE-VROPS-MIB", "vmwAlertMessage"),
        ("VMWARE-VROPS-MIB", "vmwAlertType"),
        ("VMWARE-VROPS-MIB", "vmwAlertSubtype"),
        ("VMWARE-VROPS-MIB", "vmwAlertMetricName"),
        ("VMWARE-VROPS-MIB", "vmwAlertResourceKind"),
        ("VMWARE-VROPS-MIB", "vmwAlertHealth"),
        ("VMWARE-VROPS-MIB", "vmwAlertRisk"),
        ("VMWARE-VROPS-MIB", "vmwAlertEfficiency"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionName"),
        ("VMWARE-VROPS-MIB", "vmwAlertDefinitionDesc"),
        ("VMWARE-VROPS-MIB", "vmwAlertImpact"),
        ("VMWARE-VROPS-MIB", "vmwAlertNotificationRules"))
)
if mibBuilder.loadTexts:
    vmwTrapTest.setStatus(
        "current"
    )


# Notifications groups

vmwVROPSNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99, 2, 2)
)
vmwVROPSNotificationGroup.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwTrapTest"),
        ("VMWARE-VROPS-MIB", "vmwTrapProblemActive"),
        ("VMWARE-VROPS-MIB", "vmwTrapProblemClear"),
        ("VMWARE-VROPS-MIB", "vmwTrapProblemChange"))
)
if mibBuilder.loadTexts:
    vmwVROPSNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwVROPSMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 50, 1, 99, 1, 1)
)
vmwVROPSMIBBasicCompliance.setObjects(
      *(("VMWARE-VROPS-MIB", "vmwVROPSNotificationInfoGroup"),
        ("VMWARE-VROPS-MIB", "vmwVROPSNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwVROPSMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-VROPS-MIB",
    **{"vmwVropsMIB": vmwVropsMIB,
       "vmwAlertTrap": vmwAlertTrap,
       "vmwTrapProblemActive": vmwTrapProblemActive,
       "vmwTrapProblemClear": vmwTrapProblemClear,
       "vmwTrapProblemChange": vmwTrapProblemChange,
       "vmwTrapTest": vmwTrapTest,
       "vmwGenericAlertData": vmwGenericAlertData,
       "vmwAlertAliveServerName": vmwAlertAliveServerName,
       "vmwAlertEntityName": vmwAlertEntityName,
       "vmwAlertEntityType": vmwAlertEntityType,
       "vmwAlertTimestamp": vmwAlertTimestamp,
       "vmwAlertCriticality": vmwAlertCriticality,
       "vmwAlertRootCause": vmwAlertRootCause,
       "vmwAlertURL": vmwAlertURL,
       "vmwAlertID": vmwAlertID,
       "vmwAlertMessage": vmwAlertMessage,
       "vmwAlertType": vmwAlertType,
       "vmwAlertSubtype": vmwAlertSubtype,
       "vmwAlertHealth": vmwAlertHealth,
       "vmwAlertRisk": vmwAlertRisk,
       "vmwAlertEfficiency": vmwAlertEfficiency,
       "vmwAlertMetricName": vmwAlertMetricName,
       "vmwAlertResourceKind": vmwAlertResourceKind,
       "vmwAlertDefinitionName": vmwAlertDefinitionName,
       "vmwAlertDefinitionDesc": vmwAlertDefinitionDesc,
       "vmwAlertImpact": vmwAlertImpact,
       "vmwAlertNotificationRules": vmwAlertNotificationRules,
       "vmwVROPSMIBConformance": vmwVROPSMIBConformance,
       "vmwVROPSMIBCompliances": vmwVROPSMIBCompliances,
       "vmwVROPSMIBBasicCompliance": vmwVROPSMIBBasicCompliance,
       "vmwVROPSMIBGroups": vmwVROPSMIBGroups,
       "vmwVROPSNotificationInfoGroup": vmwVROPSNotificationInfoGroup,
       "vmwVROPSNotificationGroup": vmwVROPSNotificationGroup}
)
