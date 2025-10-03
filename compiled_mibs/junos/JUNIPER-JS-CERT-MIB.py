# SNMP MIB module (JUNIPER-JS-CERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-JS-CERT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:25 2025
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

(jnxJsCertificates,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsCertificates")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsCertificateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxJsCertificateMIB.setRevisions(
        ("2007-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsCertificateObjects_ObjectIdentity = ObjectIdentity
jnxJsCertificateObjects = _JnxJsCertificateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1)
)
_JnxJsLoadedCaCertTable_Object = MibTable
jnxJsLoadedCaCertTable = _JnxJsLoadedCaCertTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertTable.setStatus("current")
_JnxJsLoadedCaCertEntry_Object = MibTableRow
jnxJsLoadedCaCertEntry = _JnxJsLoadedCaCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1)
)
jnxJsLoadedCaCertEntry.setIndexNames(
    (1, "JUNIPER-JS-CERT-MIB", "jnxJsLoadedCaCertName"),
)
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertEntry.setStatus("current")


class _JnxJsLoadedCaCertName_Type(DisplayString):
    """Custom type jnxJsLoadedCaCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsLoadedCaCertName_Type.__name__ = "DisplayString"
_JnxJsLoadedCaCertName_Object = MibTableColumn
jnxJsLoadedCaCertName = _JnxJsLoadedCaCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 1),
    _JnxJsLoadedCaCertName_Type()
)
jnxJsLoadedCaCertName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertName.setStatus("current")


class _JnxJsLoadedCaCertSubject_Type(DisplayString):
    """Custom type jnxJsLoadedCaCertSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsLoadedCaCertSubject_Type.__name__ = "DisplayString"
_JnxJsLoadedCaCertSubject_Object = MibTableColumn
jnxJsLoadedCaCertSubject = _JnxJsLoadedCaCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 2),
    _JnxJsLoadedCaCertSubject_Type()
)
jnxJsLoadedCaCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertSubject.setStatus("current")
_JnxJsLoadedCaCertExpire_Type = DateAndTime
_JnxJsLoadedCaCertExpire_Object = MibTableColumn
jnxJsLoadedCaCertExpire = _JnxJsLoadedCaCertExpire_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 3),
    _JnxJsLoadedCaCertExpire_Type()
)
jnxJsLoadedCaCertExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertExpire.setStatus("current")


class _JnxJsLoadedCaCertIssuer_Type(DisplayString):
    """Custom type jnxJsLoadedCaCertIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsLoadedCaCertIssuer_Type.__name__ = "DisplayString"
_JnxJsLoadedCaCertIssuer_Object = MibTableColumn
jnxJsLoadedCaCertIssuer = _JnxJsLoadedCaCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 1, 1, 4),
    _JnxJsLoadedCaCertIssuer_Type()
)
jnxJsLoadedCaCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedCaCertIssuer.setStatus("current")
_JnxJsLoadedLocalCertTable_Object = MibTable
jnxJsLoadedLocalCertTable = _JnxJsLoadedLocalCertTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertTable.setStatus("current")
_JnxJsLoadedLocalCertEntry_Object = MibTableRow
jnxJsLoadedLocalCertEntry = _JnxJsLoadedLocalCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1)
)
jnxJsLoadedLocalCertEntry.setIndexNames(
    (1, "JUNIPER-JS-CERT-MIB", "jnxJsLoadedLocalCertName"),
)
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertEntry.setStatus("current")


class _JnxJsLoadedLocalCertName_Type(DisplayString):
    """Custom type jnxJsLoadedLocalCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsLoadedLocalCertName_Type.__name__ = "DisplayString"
_JnxJsLoadedLocalCertName_Object = MibTableColumn
jnxJsLoadedLocalCertName = _JnxJsLoadedLocalCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 1),
    _JnxJsLoadedLocalCertName_Type()
)
jnxJsLoadedLocalCertName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertName.setStatus("current")


class _JnxJsLoadedLocalCertSubject_Type(DisplayString):
    """Custom type jnxJsLoadedLocalCertSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsLoadedLocalCertSubject_Type.__name__ = "DisplayString"
_JnxJsLoadedLocalCertSubject_Object = MibTableColumn
jnxJsLoadedLocalCertSubject = _JnxJsLoadedLocalCertSubject_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 2),
    _JnxJsLoadedLocalCertSubject_Type()
)
jnxJsLoadedLocalCertSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertSubject.setStatus("current")
_JnxJsLoadedLocalCertExpire_Type = DateAndTime
_JnxJsLoadedLocalCertExpire_Object = MibTableColumn
jnxJsLoadedLocalCertExpire = _JnxJsLoadedLocalCertExpire_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 3),
    _JnxJsLoadedLocalCertExpire_Type()
)
jnxJsLoadedLocalCertExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertExpire.setStatus("current")


class _JnxJsLoadedLocalCertIssuer_Type(DisplayString):
    """Custom type jnxJsLoadedLocalCertIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxJsLoadedLocalCertIssuer_Type.__name__ = "DisplayString"
_JnxJsLoadedLocalCertIssuer_Object = MibTableColumn
jnxJsLoadedLocalCertIssuer = _JnxJsLoadedLocalCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 1, 2, 1, 4),
    _JnxJsLoadedLocalCertIssuer_Type()
)
jnxJsLoadedLocalCertIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsLoadedLocalCertIssuer.setStatus("current")
_JnxJsCertificateNotifications_ObjectIdentity = ObjectIdentity
jnxJsCertificateNotifications = _JnxJsCertificateNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2)
)
_JnxJsCertNotificationType_ObjectIdentity = ObjectIdentity
jnxJsCertNotificationType = _JnxJsCertNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2, 1)
)
_JnxJsCertNotificationObj_ObjectIdentity = ObjectIdentity
jnxJsCertNotificationObj = _JnxJsCertNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2, 2)
)
_JnxJsCertName_Type = DisplayString
_JnxJsCertName_Object = MibScalar
jnxJsCertName = _JnxJsCertName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2, 2, 1),
    _JnxJsCertName_Type()
)
jnxJsCertName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsCertName.setStatus("current")
_JnxJsCertExpireTime_Type = DateAndTime
_JnxJsCertExpireTime_Object = MibScalar
jnxJsCertExpireTime = _JnxJsCertExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2, 2, 2),
    _JnxJsCertExpireTime_Type()
)
jnxJsCertExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsCertExpireTime.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsCertExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 3, 1, 2, 1, 1)
)
jnxJsCertExpiring.setObjects(
      *(("JUNIPER-JS-CERT-MIB", "jnxJsCertName"),
        ("JUNIPER-JS-CERT-MIB", "jnxJsCertExpireTime"))
)
if mibBuilder.loadTexts:
    jnxJsCertExpiring.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-CERT-MIB",
    **{"jnxJsCertificateMIB": jnxJsCertificateMIB,
       "jnxJsCertificateObjects": jnxJsCertificateObjects,
       "jnxJsLoadedCaCertTable": jnxJsLoadedCaCertTable,
       "jnxJsLoadedCaCertEntry": jnxJsLoadedCaCertEntry,
       "jnxJsLoadedCaCertName": jnxJsLoadedCaCertName,
       "jnxJsLoadedCaCertSubject": jnxJsLoadedCaCertSubject,
       "jnxJsLoadedCaCertExpire": jnxJsLoadedCaCertExpire,
       "jnxJsLoadedCaCertIssuer": jnxJsLoadedCaCertIssuer,
       "jnxJsLoadedLocalCertTable": jnxJsLoadedLocalCertTable,
       "jnxJsLoadedLocalCertEntry": jnxJsLoadedLocalCertEntry,
       "jnxJsLoadedLocalCertName": jnxJsLoadedLocalCertName,
       "jnxJsLoadedLocalCertSubject": jnxJsLoadedLocalCertSubject,
       "jnxJsLoadedLocalCertExpire": jnxJsLoadedLocalCertExpire,
       "jnxJsLoadedLocalCertIssuer": jnxJsLoadedLocalCertIssuer,
       "jnxJsCertificateNotifications": jnxJsCertificateNotifications,
       "jnxJsCertNotificationType": jnxJsCertNotificationType,
       "jnxJsCertExpiring": jnxJsCertExpiring,
       "jnxJsCertNotificationObj": jnxJsCertNotificationObj,
       "jnxJsCertName": jnxJsCertName,
       "jnxJsCertExpireTime": jnxJsCertExpireTime}
)
