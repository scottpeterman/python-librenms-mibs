# SNMP MIB module (ALGSMXS-v0-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\algcom\ALGSMXS-v0-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:14 2025
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

_Algcom_ObjectIdentity = ObjectIdentity
algcom = _Algcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136)
)
_SMxSOIDs_ObjectIdentity = ObjectIdentity
SMxSOIDs = _SMxSOIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100)
)
_SensorNames_ObjectIdentity = ObjectIdentity
SensorNames = _SensorNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 1)
)
_SensorDescriptions_ObjectIdentity = ObjectIdentity
SensorDescriptions = _SensorDescriptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 2)
)
_SensorValues_ObjectIdentity = ObjectIdentity
SensorValues = _SensorValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 3)
)
_SensorUnits_ObjectIdentity = ObjectIdentity
SensorUnits = _SensorUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 4)
)
_SensorThrMin_ObjectIdentity = ObjectIdentity
SensorThrMin = _SensorThrMin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 5)
)
_SensorThrMax_ObjectIdentity = ObjectIdentity
SensorThrMax = _SensorThrMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 100, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALGSMXS-v0-MIB",
    **{"algcom": algcom,
       "SMxSOIDs": SMxSOIDs,
       "SensorNames": SensorNames,
       "SensorDescriptions": SensorDescriptions,
       "SensorValues": SensorValues,
       "SensorUnits": SensorUnits,
       "SensorThrMin": SensorThrMin,
       "SensorThrMax": SensorThrMax}
)
