# SNMP MIB module (JUNIPER-MOBILE-GW-SGW-MFWD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-MOBILE-GW-SGW-MFWD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:19 2025
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

(jnxMobileGatewaySgw,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewaySgw")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwName,) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxMbgSgwMfwdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSgwMfwdNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSgwMfwdNotifications = _JnxMbgSgwMfwdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0)
)
_JnxMbgSgwMfwdNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSgwMfwdNotificationVars = _JnxMbgSgwMfwdNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1)
)


class _JnxMbgSgwMfwdServicePicName_Type(DisplayString):
    """Custom type jnxMbgSgwMfwdServicePicName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 15),
    )


_JnxMbgSgwMfwdServicePicName_Type.__name__ = "DisplayString"
_JnxMbgSgwMfwdServicePicName_Object = MibScalar
jnxMbgSgwMfwdServicePicName = _JnxMbgSgwMfwdServicePicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 1),
    _JnxMbgSgwMfwdServicePicName_Type()
)
jnxMbgSgwMfwdServicePicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdServicePicName.setStatus("current")
_JnxMbgSgwMfwdBufMemLimit_Type = Gauge32
_JnxMbgSgwMfwdBufMemLimit_Object = MibScalar
jnxMbgSgwMfwdBufMemLimit = _JnxMbgSgwMfwdBufMemLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 2),
    _JnxMbgSgwMfwdBufMemLimit_Type()
)
jnxMbgSgwMfwdBufMemLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemLimit.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemLimit.setUnits("percent")

# Managed Objects groups


# Notification objects

jnxMbgSgwMfwdBufMemThresRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 1)
)
jnxMbgSgwMfwdBufMemThresRaise.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemThresRaise.setStatus(
        "current"
    )

jnxMbgSgwMfwdBufMemThresClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 2)
)
jnxMbgSgwMfwdBufMemThresClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"),
        ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMfwdBufMemThresClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GW-SGW-MFWD-MIB",
    **{"jnxMbgSgwMfwdMib": jnxMbgSgwMfwdMib,
       "jnxMbgSgwMfwdNotifications": jnxMbgSgwMfwdNotifications,
       "jnxMbgSgwMfwdBufMemThresRaise": jnxMbgSgwMfwdBufMemThresRaise,
       "jnxMbgSgwMfwdBufMemThresClear": jnxMbgSgwMfwdBufMemThresClear,
       "jnxMbgSgwMfwdNotificationVars": jnxMbgSgwMfwdNotificationVars,
       "jnxMbgSgwMfwdServicePicName": jnxMbgSgwMfwdServicePicName,
       "jnxMbgSgwMfwdBufMemLimit": jnxMbgSgwMfwdBufMemLimit}
)
