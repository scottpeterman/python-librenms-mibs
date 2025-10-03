# SNMP MIB module (CTRON-BUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CTRON-BUS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:36 2025
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

(ctAtmfLanEmulation,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctAtmfLanEmulation")

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


# MODULE-IDENTITY


# Types definitions



class CtLaneDebugLevel(Integer32):
    """Custom type CtLaneDebugLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("all", 2),
          ("error", 3),
          ("warning", 4),
          ("informational", 5),
          ("detailed", 6),
          ("trace", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtBus_ObjectIdentity = ObjectIdentity
ctBus = _CtBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4)
)
_CtBusConfGroup_ObjectIdentity = ObjectIdentity
ctBusConfGroup = _CtBusConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1)
)


class _CtBusDSStatus_Type(Integer32):
    """Custom type ctBusDSStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("connectionLost", 2),
          ("unknown", 3))
    )


_CtBusDSStatus_Type.__name__ = "Integer32"
_CtBusDSStatus_Object = MibScalar
ctBusDSStatus = _CtBusDSStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 1),
    _CtBusDSStatus_Type()
)
ctBusDSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBusDSStatus.setStatus("mandatory")


class _CtBusUNIVersion_Type(Integer32):
    """Custom type ctBusUNIVersion based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 1),
          ("uni30", 2),
          ("uni31", 3),
          ("uni40", 4))
    )


_CtBusUNIVersion_Type.__name__ = "Integer32"
_CtBusUNIVersion_Object = MibScalar
ctBusUNIVersion = _CtBusUNIVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 2),
    _CtBusUNIVersion_Type()
)
ctBusUNIVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctBusUNIVersion.setStatus("mandatory")


class _CtBusLaneDbgOutputFile_Type(DisplayString):
    """Custom type ctBusLaneDbgOutputFile based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtBusLaneDbgOutputFile_Type.__name__ = "DisplayString"
_CtBusLaneDbgOutputFile_Object = MibScalar
ctBusLaneDbgOutputFile = _CtBusLaneDbgOutputFile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 3),
    _CtBusLaneDbgOutputFile_Type()
)
ctBusLaneDbgOutputFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBusLaneDbgOutputFile.setStatus("mandatory")


class _CtBusLaneDbgConnectionServices_Type(CtLaneDebugLevel):
    """Custom type ctBusLaneDbgConnectionServices based on CtLaneDebugLevel"""
    defaultValue = 1


_CtBusLaneDbgConnectionServices_Type.__name__ = "CtLaneDebugLevel"
_CtBusLaneDbgConnectionServices_Object = MibScalar
ctBusLaneDbgConnectionServices = _CtBusLaneDbgConnectionServices_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 4),
    _CtBusLaneDbgConnectionServices_Type()
)
ctBusLaneDbgConnectionServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBusLaneDbgConnectionServices.setStatus("mandatory")


class _CtBusLaneDbgSNMP_Type(CtLaneDebugLevel):
    """Custom type ctBusLaneDbgSNMP based on CtLaneDebugLevel"""
    defaultValue = 1


_CtBusLaneDbgSNMP_Type.__name__ = "CtLaneDebugLevel"
_CtBusLaneDbgSNMP_Object = MibScalar
ctBusLaneDbgSNMP = _CtBusLaneDbgSNMP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 5),
    _CtBusLaneDbgSNMP_Type()
)
ctBusLaneDbgSNMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBusLaneDbgSNMP.setStatus("mandatory")


class _CtBusLaneDbgBUS_Type(CtLaneDebugLevel):
    """Custom type ctBusLaneDbgBUS based on CtLaneDebugLevel"""
    defaultValue = 1


_CtBusLaneDbgBUS_Type.__name__ = "CtLaneDebugLevel"
_CtBusLaneDbgBUS_Object = MibScalar
ctBusLaneDbgBUS = _CtBusLaneDbgBUS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4, 1, 6),
    _CtBusLaneDbgBUS_Type()
)
ctBusLaneDbgBUS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctBusLaneDbgBUS.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-BUS-MIB",
    **{"CtLaneDebugLevel": CtLaneDebugLevel,
       "ctBus": ctBus,
       "ctBusConfGroup": ctBusConfGroup,
       "ctBusDSStatus": ctBusDSStatus,
       "ctBusUNIVersion": ctBusUNIVersion,
       "ctBusLaneDbgOutputFile": ctBusLaneDbgOutputFile,
       "ctBusLaneDbgConnectionServices": ctBusLaneDbgConnectionServices,
       "ctBusLaneDbgSNMP": ctBusLaneDbgSNMP,
       "ctBusLaneDbgBUS": ctBusLaneDbgBUS}
)
