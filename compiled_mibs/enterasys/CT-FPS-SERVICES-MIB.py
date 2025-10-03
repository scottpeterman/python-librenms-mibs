# SNMP MIB module (CT-FPS-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\enterasys\CT-FPS-SERVICES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:40:16 2025
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

(ctFPSServices,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFPSServices")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtFPSActivity_ObjectIdentity = ObjectIdentity
ctFPSActivity = _CtFPSActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1)
)


class _CtLookUpFwdActivity_Type(Integer32):
    """Custom type ctLookUpFwdActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CtLookUpFwdActivity_Type.__name__ = "Integer32"
_CtLookUpFwdActivity_Object = MibScalar
ctLookUpFwdActivity = _CtLookUpFwdActivity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 1),
    _CtLookUpFwdActivity_Type()
)
ctLookUpFwdActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctLookUpFwdActivity.setStatus("mandatory")


class _CtINBActivity_Type(Integer32):
    """Custom type ctINBActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CtINBActivity_Type.__name__ = "Integer32"
_CtINBActivity_Object = MibScalar
ctINBActivity = _CtINBActivity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15, 1, 2),
    _CtINBActivity_Type()
)
ctINBActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctINBActivity.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-FPS-SERVICES-MIB",
    **{"ctFPSActivity": ctFPSActivity,
       "ctLookUpFwdActivity": ctLookUpFwdActivity,
       "ctINBActivity": ctINBActivity}
)
