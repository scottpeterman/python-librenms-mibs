# SNMP MIB module (MOXA-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-GENERAL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:04 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

general = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602)
)
if mibBuilder.loadTexts:
    general.setRevisions(
        ("2022-02-17 00:00",
         "2019-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_SystemManagement_ObjectIdentity = ObjectIdentity
systemManagement = _SystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1)
)
_NetworkConfiguration_ObjectIdentity = ObjectIdentity
networkConfiguration = _NetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 2)
)
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 3)
)
_NetworkManagement_ObjectIdentity = ObjectIdentity
networkManagement = _NetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 4)
)
_DeviceSecurity_ObjectIdentity = ObjectIdentity
deviceSecurity = _DeviceSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 5)
)
_Authentication_ObjectIdentity = ObjectIdentity
authentication = _Authentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 6)
)
_EventNotification_ObjectIdentity = ObjectIdentity
eventNotification = _EventNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 7)
)
_DeviceDiagnostics_ObjectIdentity = ObjectIdentity
deviceDiagnostics = _DeviceDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 8)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-GENERAL-MIB",
    **{"moxa": moxa,
       "general": general,
       "systemManagement": systemManagement,
       "networkConfiguration": networkConfiguration,
       "time": time,
       "networkManagement": networkManagement,
       "deviceSecurity": deviceSecurity,
       "authentication": authentication,
       "eventNotification": eventNotification,
       "deviceDiagnostics": deviceDiagnostics}
)
