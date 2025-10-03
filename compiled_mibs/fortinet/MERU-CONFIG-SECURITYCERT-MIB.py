# SNMP MIB module (MERU-CONFIG-SECURITYCERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-SECURITYCERT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:10 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigSecurityCert = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwSslCertInput_ObjectIdentity = ObjectIdentity
mwSslCertInput = _MwSslCertInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2)
)


class _MwSslCertInputCertificateName_Type(DisplayString):
    """Custom type mwSslCertInputCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwSslCertInputCertificateName_Type.__name__ = "DisplayString"
_MwSslCertInputCertificateName_Object = MibScalar
mwSslCertInputCertificateName = _MwSslCertInputCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 1),
    _MwSslCertInputCertificateName_Type()
)
mwSslCertInputCertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSslCertInputCertificateName.setStatus("current")


class _MwSslCertInputPfxPassword_Type(DisplayString):
    """Custom type mwSslCertInputPfxPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwSslCertInputPfxPassword_Type.__name__ = "DisplayString"
_MwSslCertInputPfxPassword_Object = MibScalar
mwSslCertInputPfxPassword = _MwSslCertInputPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 2),
    _MwSslCertInputPfxPassword_Type()
)
mwSslCertInputPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSslCertInputPfxPassword.setStatus("current")
_MwSslCert_ObjectIdentity = ObjectIdentity
mwSslCert = _MwSslCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3)
)


class _MwSslCertCertificateName_Type(DisplayString):
    """Custom type mwSslCertCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwSslCertCertificateName_Type.__name__ = "DisplayString"
_MwSslCertCertificateName_Object = MibScalar
mwSslCertCertificateName = _MwSslCertCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 1),
    _MwSslCertCertificateName_Type()
)
mwSslCertCertificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslCertCertificateName.setStatus("current")
_MwSslCertCertFormattedText_Type = DisplayString
_MwSslCertCertFormattedText_Object = MibScalar
mwSslCertCertFormattedText = _MwSslCertCertFormattedText_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 2),
    _MwSslCertCertFormattedText_Type()
)
mwSslCertCertFormattedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslCertCertFormattedText.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-SECURITYCERT-MIB",
    **{"mwConfigSecurityCert": mwConfigSecurityCert,
       "mwSslCertInput": mwSslCertInput,
       "mwSslCertInputCertificateName": mwSslCertInputCertificateName,
       "mwSslCertInputPfxPassword": mwSslCertInputPfxPassword,
       "mwSslCert": mwSslCert,
       "mwSslCertCertificateName": mwSslCertCertificateName,
       "mwSslCertCertFormattedText": mwSslCertCertFormattedText}
)
