# SNMP MIB module (GAM-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\positron\GAM-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:51 2025
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

(gamProducts,) = mibBuilder.importSymbols(
    "POSITRON-SMI",
    "gamProducts")

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

gamProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1)
)
if mibBuilder.loadTexts:
    gamProductsMIB.setRevisions(
        ("2017-07-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gam4MRX_ObjectIdentity = ObjectIdentity
gam4MRX = _Gam4MRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 1)
)
_Gam4CRX_ObjectIdentity = ObjectIdentity
gam4CRX = _Gam4CRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 2)
)
_Gam4CRXLC_ObjectIdentity = ObjectIdentity
gam4CRXLC = _Gam4CRXLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 3)
)
_Gam4CRXOPTI_ObjectIdentity = ObjectIdentity
gam4CRXOPTI = _Gam4CRXOPTI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 4)
)
_Gam4MRXLC_ObjectIdentity = ObjectIdentity
gam4MRXLC = _Gam4MRXLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 5)
)
_Gam4MRXOPTI_ObjectIdentity = ObjectIdentity
gam4MRXOPTI = _Gam4MRXOPTI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 6)
)
_Gam8MRX_ObjectIdentity = ObjectIdentity
gam8MRX = _Gam8MRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 7)
)
_Gam8MRXLC_ObjectIdentity = ObjectIdentity
gam8MRXLC = _Gam8MRXLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 8)
)
_Gam8MRXOPTI_ObjectIdentity = ObjectIdentity
gam8MRXOPTI = _Gam8MRXOPTI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 9)
)
_Gam8CRX_ObjectIdentity = ObjectIdentity
gam8CRX = _Gam8CRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 10)
)
_Gam8CRXLC_ObjectIdentity = ObjectIdentity
gam8CRXLC = _Gam8CRXLC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 11)
)
_Gam8CRXOPTI_ObjectIdentity = ObjectIdentity
gam8CRXOPTI = _Gam8CRXOPTI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 12)
)
_Gam12M_ObjectIdentity = ObjectIdentity
gam12M = _Gam12M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 13)
)
_Gam12C_ObjectIdentity = ObjectIdentity
gam12C = _Gam12C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 14)
)
_Gam24M_ObjectIdentity = ObjectIdentity
gam24M = _Gam24M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 15)
)
_Gam24C_ObjectIdentity = ObjectIdentity
gam24C = _Gam24C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 16)
)
_Gam4MX_ObjectIdentity = ObjectIdentity
gam4MX = _Gam4MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 17)
)
_Gam4CX_ObjectIdentity = ObjectIdentity
gam4CX = _Gam4CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 18)
)
_Gam8MX_ObjectIdentity = ObjectIdentity
gam8MX = _Gam8MX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 19)
)
_Gam8CX_ObjectIdentity = ObjectIdentity
gam8CX = _Gam8CX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 20)
)
_Gam8MVXA_ObjectIdentity = ObjectIdentity
gam8MVXA = _Gam8MVXA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 21)
)
_Gam8MVXG_ObjectIdentity = ObjectIdentity
gam8MVXG = _Gam8MVXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 22)
)
_Gam8MDVXA_ObjectIdentity = ObjectIdentity
gam8MDVXA = _Gam8MDVXA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 23)
)
_Gam8MDVXG_ObjectIdentity = ObjectIdentity
gam8MDVXG = _Gam8MDVXG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 24)
)
_Gam4MRXLBE_ObjectIdentity = ObjectIdentity
gam4MRXLBE = _Gam4MRXLBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 25)
)
_Gam8MRXLBE_ObjectIdentity = ObjectIdentity
gam8MRXLBE = _Gam8MRXLBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 26)
)
_Gam12MLBE_ObjectIdentity = ObjectIdentity
gam12MLBE = _Gam12MLBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20095, 2000, 1, 27)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GAM-PRODUCTS-MIB",
    **{"gamProductsMIB": gamProductsMIB,
       "gam4MRX": gam4MRX,
       "gam4CRX": gam4CRX,
       "gam4CRXLC": gam4CRXLC,
       "gam4CRXOPTI": gam4CRXOPTI,
       "gam4MRXLC": gam4MRXLC,
       "gam4MRXOPTI": gam4MRXOPTI,
       "gam8MRX": gam8MRX,
       "gam8MRXLC": gam8MRXLC,
       "gam8MRXOPTI": gam8MRXOPTI,
       "gam8CRX": gam8CRX,
       "gam8CRXLC": gam8CRXLC,
       "gam8CRXOPTI": gam8CRXOPTI,
       "gam12M": gam12M,
       "gam12C": gam12C,
       "gam24M": gam24M,
       "gam24C": gam24C,
       "gam4MX": gam4MX,
       "gam4CX": gam4CX,
       "gam8MX": gam8MX,
       "gam8CX": gam8CX,
       "gam8MVXA": gam8MVXA,
       "gam8MVXG": gam8MVXG,
       "gam8MDVXA": gam8MDVXA,
       "gam8MDVXG": gam8MDVXG,
       "gam4MRXLBE": gam4MRXLBE,
       "gam8MRXLBE": gam8MRXLBE,
       "gam12MLBE": gam12MLBE}
)
