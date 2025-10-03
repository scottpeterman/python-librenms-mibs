# SNMP MIB module (DATACOM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\datacom\DATACOM-SMI
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:16 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Datacom_ObjectIdentity = ObjectIdentity
datacom = _Datacom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709)
)
_DatacomRegistrations_ObjectIdentity = ObjectIdentity
datacomRegistrations = _DatacomRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1)
)
_DatacomModules_ObjectIdentity = ObjectIdentity
datacomModules = _DatacomModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 1)
)
_DatacomManagementCards_ObjectIdentity = ObjectIdentity
datacomManagementCards = _DatacomManagementCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 2)
)
_DatacomModems_ObjectIdentity = ObjectIdentity
datacomModems = _DatacomModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 3)
)
_DatacomAccessDevices_ObjectIdentity = ObjectIdentity
datacomAccessDevices = _DatacomAccessDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 5)
)
_DatacomDevices_ObjectIdentity = ObjectIdentity
datacomDevices = _DatacomDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 6)
)
_DatacomGenericMIBs_ObjectIdentity = ObjectIdentity
datacomGenericMIBs = _DatacomGenericMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2)
)
_DatacomProductsMIBs_ObjectIdentity = ObjectIdentity
datacomProductsMIBs = _DatacomProductsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3)
)
_DatacomModemsMIBs_ObjectIdentity = ObjectIdentity
datacomModemsMIBs = _DatacomModemsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 3)
)
_DatacomAccessDevicesMIBs_ObjectIdentity = ObjectIdentity
datacomAccessDevicesMIBs = _DatacomAccessDevicesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 5)
)
_DatacomDevicesMIBs_ObjectIdentity = ObjectIdentity
datacomDevicesMIBs = _DatacomDevicesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6)
)
_DatacomExperimental_ObjectIdentity = ObjectIdentity
datacomExperimental = _DatacomExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 4)
)
_DatacomExpGenericMIBs_ObjectIdentity = ObjectIdentity
datacomExpGenericMIBs = _DatacomExpGenericMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 4, 2)
)
_DatacomExpProductsMIBs_ObjectIdentity = ObjectIdentity
datacomExpProductsMIBs = _DatacomExpProductsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 4, 3)
)
_DatacomExpModemsMIBs_ObjectIdentity = ObjectIdentity
datacomExpModemsMIBs = _DatacomExpModemsMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 4, 3, 3)
)
_DatacomExpAccessDevicesMIBs_ObjectIdentity = ObjectIdentity
datacomExpAccessDevicesMIBs = _DatacomExpAccessDevicesMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 4, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATACOM-SMI",
    **{"datacom": datacom,
       "datacomRegistrations": datacomRegistrations,
       "datacomModules": datacomModules,
       "datacomManagementCards": datacomManagementCards,
       "datacomModems": datacomModems,
       "datacomAccessDevices": datacomAccessDevices,
       "datacomDevices": datacomDevices,
       "datacomGenericMIBs": datacomGenericMIBs,
       "datacomProductsMIBs": datacomProductsMIBs,
       "datacomModemsMIBs": datacomModemsMIBs,
       "datacomAccessDevicesMIBs": datacomAccessDevicesMIBs,
       "datacomDevicesMIBs": datacomDevicesMIBs,
       "datacomExperimental": datacomExperimental,
       "datacomExpGenericMIBs": datacomExpGenericMIBs,
       "datacomExpProductsMIBs": datacomExpProductsMIBs,
       "datacomExpModemsMIBs": datacomExpModemsMIBs,
       "datacomExpAccessDevicesMIBs": datacomExpAccessDevicesMIBs}
)
