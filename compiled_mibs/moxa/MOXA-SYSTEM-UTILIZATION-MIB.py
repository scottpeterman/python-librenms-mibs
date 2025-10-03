# SNMP MIB module (MOXA-SYSTEM-UTILIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-SYSTEM-UTILIZATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:06 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mxSysUtilSvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3)
)
if mibBuilder.loadTexts:
    mxSysUtilSvr.setRevisions(
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
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602)
)
_SystemManagement_ObjectIdentity = ObjectIdentity
systemManagement = _SystemManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1)
)
_UsStatus_ObjectIdentity = ObjectIdentity
usStatus = _UsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3, 2)
)
_UsStatCPUUtilization_Type = Unsigned32
_UsStatCPUUtilization_Object = MibScalar
usStatCPUUtilization = _UsStatCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3, 2, 1),
    _UsStatCPUUtilization_Type()
)
usStatCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usStatCPUUtilization.setStatus("current")
_UsStatMemorySize_Type = Unsigned32
_UsStatMemorySize_Object = MibScalar
usStatMemorySize = _UsStatMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3, 2, 2),
    _UsStatMemorySize_Type()
)
usStatMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usStatMemorySize.setStatus("current")
_UsStatMemoryUtilization_Type = Unsigned32
_UsStatMemoryUtilization_Object = MibScalar
usStatMemoryUtilization = _UsStatMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3, 2, 3),
    _UsStatMemoryUtilization_Type()
)
usStatMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usStatMemoryUtilization.setStatus("current")
_UsStatPowerConsumption_Type = Unsigned32
_UsStatPowerConsumption_Object = MibScalar
usStatPowerConsumption = _UsStatPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 602, 1, 3, 2, 4),
    _UsStatPowerConsumption_Type()
)
usStatPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usStatPowerConsumption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-SYSTEM-UTILIZATION-MIB",
    **{"moxa": moxa,
       "general": general,
       "systemManagement": systemManagement,
       "mxSysUtilSvr": mxSysUtilSvr,
       "usStatus": usStatus,
       "usStatCPUUtilization": usStatCPUUtilization,
       "usStatMemorySize": usStatMemorySize,
       "usStatMemoryUtilization": usStatMemoryUtilization,
       "usStatPowerConsumption": usStatPowerConsumption}
)
