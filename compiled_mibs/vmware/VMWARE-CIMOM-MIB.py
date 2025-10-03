# SNMP MIB module (VMWARE-CIMOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-CIMOM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:16 2025
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

(vmwEnvIndicationTime,) = mibBuilder.importSymbols(
    "VMWARE-ENV-MIB",
    "vmwEnvIndicationTime")

(vmwProductSpecific,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwProductSpecific")


# MODULE-IDENTITY

vmwCIMOMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 10)
)
if mibBuilder.loadTexts:
    vmwCIMOMMIB.setRevisions(
        ("2010-08-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwCimOm_ObjectIdentity = ObjectIdentity
vmwCimOm = _VmwCimOm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90)
)
_VmwCimOmNotifications_ObjectIdentity = ObjectIdentity
vmwCimOmNotifications = _VmwCimOmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 0)
)
_VmwCimOmMIBConformance_ObjectIdentity = ObjectIdentity
vmwCimOmMIBConformance = _VmwCimOmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2)
)
_VmwCimOmMIBCompliances_ObjectIdentity = ObjectIdentity
vmwCimOmMIBCompliances = _VmwCimOmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1)
)
_VmwCimOmMIBGroups_ObjectIdentity = ObjectIdentity
vmwCimOmMIBGroups = _VmwCimOmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2)
)

# Managed Objects groups


# Notification objects

vmwCimOmHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 0, 401)
)
vmwCimOmHeartbeat.setObjects(
    ("VMWARE-ENV-MIB", "vmwEnvIndicationTime")
)
if mibBuilder.loadTexts:
    vmwCimOmHeartbeat.setStatus(
        "current"
    )


# Notifications groups

vmwCimOmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 2, 2)
)
vmwCimOmNotificationGroup.setObjects(
    ("VMWARE-CIMOM-MIB", "vmwCimOmHeartbeat")
)
if mibBuilder.loadTexts:
    vmwCimOmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwCimOmMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 90, 2, 1, 4)
)
vmwCimOmMIBBasicCompliance.setObjects(
      *(("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"),
        ("VMWARE-CIMOM-MIB", "vmwCimOmNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwCimOmMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-CIMOM-MIB",
    **{"vmwCimOm": vmwCimOm,
       "vmwCimOmNotifications": vmwCimOmNotifications,
       "vmwCimOmHeartbeat": vmwCimOmHeartbeat,
       "vmwCimOmMIBConformance": vmwCimOmMIBConformance,
       "vmwCimOmMIBCompliances": vmwCimOmMIBCompliances,
       "vmwCimOmMIBBasicCompliance": vmwCimOmMIBBasicCompliance,
       "vmwCimOmMIBGroups": vmwCimOmMIBGroups,
       "vmwCimOmNotificationGroup": vmwCimOmNotificationGroup,
       "vmwCIMOMMIB": vmwCIMOMMIB}
)
