# SNMP MIB module (CIENA-CES-8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-CES-8021X-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:21 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(dot1xPaeSystemAuthControl,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaeSystemAuthControl")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCes8021xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42)
)
if mibBuilder.loadTexts:
    cienaCes8021xMIB.setRevisions(
        ("2017-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCes8021xConf_ObjectIdentity = ObjectIdentity
cienaCes8021xConf = _CienaCes8021xConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 1)
)
_CienaCes8021xGroups_ObjectIdentity = ObjectIdentity
cienaCes8021xGroups = _CienaCes8021xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 1, 1)
)
_CienaCes8021xCompls_ObjectIdentity = ObjectIdentity
cienaCes8021xCompls = _CienaCes8021xCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 1, 2)
)
_CienaCes8021xObjs_ObjectIdentity = ObjectIdentity
cienaCes8021xObjs = _CienaCes8021xObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2)
)
_CienaCes8021xPortTable_Object = MibTable
cienaCes8021xPortTable = _CienaCes8021xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCes8021xPortTable.setStatus("current")
_CienaCes8021xPortEntry_Object = MibTableRow
cienaCes8021xPortEntry = _CienaCes8021xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1, 1)
)
cienaCes8021xPortEntry.setIndexNames(
    (0, "CIENA-CES-8021X-MIB", "cienaCes8021xPort"),
)
if mibBuilder.loadTexts:
    cienaCes8021xPortEntry.setStatus("current")
_CienaCes8021xPort_Type = Unsigned32
_CienaCes8021xPort_Object = MibTableColumn
cienaCes8021xPort = _CienaCes8021xPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1, 1, 1),
    _CienaCes8021xPort_Type()
)
cienaCes8021xPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCes8021xPort.setStatus("current")


class _CienaCes8021xRole_Type(Integer32):
    """Custom type cienaCes8021xRole based on Integer32"""
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
        *(("none", 1),
          ("supplicant", 2),
          ("authenticator", 3),
          ("both", 4))
    )


_CienaCes8021xRole_Type.__name__ = "Integer32"
_CienaCes8021xRole_Object = MibTableColumn
cienaCes8021xRole = _CienaCes8021xRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1, 1, 2),
    _CienaCes8021xRole_Type()
)
cienaCes8021xRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xRole.setStatus("current")
_CienaCes8021xAuthPortStatsClear_Type = TruthValue
_CienaCes8021xAuthPortStatsClear_Object = MibTableColumn
cienaCes8021xAuthPortStatsClear = _CienaCes8021xAuthPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1, 1, 3),
    _CienaCes8021xAuthPortStatsClear_Type()
)
cienaCes8021xAuthPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xAuthPortStatsClear.setStatus("current")


class _CienaCes8021xNotificationAuthenticationEvent_Type(Integer32):
    """Custom type cienaCes8021xNotificationAuthenticationEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2),
          ("timeout", 3))
    )


_CienaCes8021xNotificationAuthenticationEvent_Type.__name__ = "Integer32"
_CienaCes8021xNotificationAuthenticationEvent_Object = MibTableColumn
cienaCes8021xNotificationAuthenticationEvent = _CienaCes8021xNotificationAuthenticationEvent_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 1, 1, 4),
    _CienaCes8021xNotificationAuthenticationEvent_Type()
)
cienaCes8021xNotificationAuthenticationEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCes8021xNotificationAuthenticationEvent.setStatus("current")
_CienaCes8021xSuppTable_Object = MibTable
cienaCes8021xSuppTable = _CienaCes8021xSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCes8021xSuppTable.setStatus("current")
_CienaCes8021xSuppEntry_Object = MibTableRow
cienaCes8021xSuppEntry = _CienaCes8021xSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1)
)
cienaCes8021xSuppEntry.setIndexNames(
    (0, "CIENA-CES-8021X-MIB", "cienaCes8021xSuppPort"),
)
if mibBuilder.loadTexts:
    cienaCes8021xSuppEntry.setStatus("current")
_CienaCes8021xSuppPort_Type = Unsigned32
_CienaCes8021xSuppPort_Object = MibTableColumn
cienaCes8021xSuppPort = _CienaCes8021xSuppPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 1),
    _CienaCes8021xSuppPort_Type()
)
cienaCes8021xSuppPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCes8021xSuppPort.setStatus("current")


class _CienaCes8021xSuppUserName_Type(DisplayString):
    """Custom type cienaCes8021xSuppUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCes8021xSuppUserName_Type.__name__ = "DisplayString"
_CienaCes8021xSuppUserName_Object = MibTableColumn
cienaCes8021xSuppUserName = _CienaCes8021xSuppUserName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 2),
    _CienaCes8021xSuppUserName_Type()
)
cienaCes8021xSuppUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppUserName.setStatus("current")


class _CienaCes8021xSuppPassword_Type(DisplayString):
    """Custom type cienaCes8021xSuppPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CienaCes8021xSuppPassword_Type.__name__ = "DisplayString"
_CienaCes8021xSuppPassword_Object = MibTableColumn
cienaCes8021xSuppPassword = _CienaCes8021xSuppPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 3),
    _CienaCes8021xSuppPassword_Type()
)
cienaCes8021xSuppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppPassword.setStatus("current")
_CienaCes8021xSuppPortStatsClear_Type = TruthValue
_CienaCes8021xSuppPortStatsClear_Object = MibTableColumn
cienaCes8021xSuppPortStatsClear = _CienaCes8021xSuppPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 5),
    _CienaCes8021xSuppPortStatsClear_Type()
)
cienaCes8021xSuppPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppPortStatsClear.setStatus("current")


class _CienaCes8021xSuppEAPMethod_Type(Integer32):
    """Custom type cienaCes8021xSuppEAPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eapMd5", 1)
    )


_CienaCes8021xSuppEAPMethod_Type.__name__ = "Integer32"
_CienaCes8021xSuppEAPMethod_Object = MibTableColumn
cienaCes8021xSuppEAPMethod = _CienaCes8021xSuppEAPMethod_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 10),
    _CienaCes8021xSuppEAPMethod_Type()
)
cienaCes8021xSuppEAPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppEAPMethod.setStatus("obsolete")


class _CienaCes8021xSuppEAPAllowedMethods_Type(Bits):
    """Custom type cienaCes8021xSuppEAPAllowedMethods based on Bits"""
    namedValues = NamedValues(
        *(("eapMd5", 0),
          ("eapTls", 1))
    )

_CienaCes8021xSuppEAPAllowedMethods_Type.__name__ = "Bits"
_CienaCes8021xSuppEAPAllowedMethods_Object = MibTableColumn
cienaCes8021xSuppEAPAllowedMethods = _CienaCes8021xSuppEAPAllowedMethods_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 11),
    _CienaCes8021xSuppEAPAllowedMethods_Type()
)
cienaCes8021xSuppEAPAllowedMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppEAPAllowedMethods.setStatus("current")


class _CienaCes8021xSuppOperationalState_Type(Integer32):
    """Custom type cienaCes8021xSuppOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppOperationalState_Type.__name__ = "Integer32"
_CienaCes8021xSuppOperationalState_Object = MibTableColumn
cienaCes8021xSuppOperationalState = _CienaCes8021xSuppOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 12),
    _CienaCes8021xSuppOperationalState_Type()
)
cienaCes8021xSuppOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCes8021xSuppOperationalState.setStatus("current")


class _CienaCes8021xSuppMutualAuthenticationAdminState_Type(Integer32):
    """Custom type cienaCes8021xSuppMutualAuthenticationAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppMutualAuthenticationAdminState_Type.__name__ = "Integer32"
_CienaCes8021xSuppMutualAuthenticationAdminState_Object = MibTableColumn
cienaCes8021xSuppMutualAuthenticationAdminState = _CienaCes8021xSuppMutualAuthenticationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 13),
    _CienaCes8021xSuppMutualAuthenticationAdminState_Type()
)
cienaCes8021xSuppMutualAuthenticationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppMutualAuthenticationAdminState.setStatus("current")


class _CienaCes8021xSuppCheckCertificateTimeAdminState_Type(Integer32):
    """Custom type cienaCes8021xSuppCheckCertificateTimeAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppCheckCertificateTimeAdminState_Type.__name__ = "Integer32"
_CienaCes8021xSuppCheckCertificateTimeAdminState_Object = MibTableColumn
cienaCes8021xSuppCheckCertificateTimeAdminState = _CienaCes8021xSuppCheckCertificateTimeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 14),
    _CienaCes8021xSuppCheckCertificateTimeAdminState_Type()
)
cienaCes8021xSuppCheckCertificateTimeAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppCheckCertificateTimeAdminState.setStatus("current")


class _CienaCes8021xSuppMutualAuthenticationOperState_Type(Integer32):
    """Custom type cienaCes8021xSuppMutualAuthenticationOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppMutualAuthenticationOperState_Type.__name__ = "Integer32"
_CienaCes8021xSuppMutualAuthenticationOperState_Object = MibTableColumn
cienaCes8021xSuppMutualAuthenticationOperState = _CienaCes8021xSuppMutualAuthenticationOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 15),
    _CienaCes8021xSuppMutualAuthenticationOperState_Type()
)
cienaCes8021xSuppMutualAuthenticationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCes8021xSuppMutualAuthenticationOperState.setStatus("current")


class _CienaCes8021xSuppCheckCertificateTimeOperState_Type(Integer32):
    """Custom type cienaCes8021xSuppCheckCertificateTimeOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppCheckCertificateTimeOperState_Type.__name__ = "Integer32"
_CienaCes8021xSuppCheckCertificateTimeOperState_Object = MibTableColumn
cienaCes8021xSuppCheckCertificateTimeOperState = _CienaCes8021xSuppCheckCertificateTimeOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 16),
    _CienaCes8021xSuppCheckCertificateTimeOperState_Type()
)
cienaCes8021xSuppCheckCertificateTimeOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCes8021xSuppCheckCertificateTimeOperState.setStatus("current")


class _CienaCes8021xSuppDeviceCertificateStatus_Type(Integer32):
    """Custom type cienaCes8021xSuppDeviceCertificateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("notPresent", 3))
    )


_CienaCes8021xSuppDeviceCertificateStatus_Type.__name__ = "Integer32"
_CienaCes8021xSuppDeviceCertificateStatus_Object = MibTableColumn
cienaCes8021xSuppDeviceCertificateStatus = _CienaCes8021xSuppDeviceCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 17),
    _CienaCes8021xSuppDeviceCertificateStatus_Type()
)
cienaCes8021xSuppDeviceCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCes8021xSuppDeviceCertificateStatus.setStatus("current")


class _CienaCes8021xSuppSecret_Type(OctetString):
    """Custom type cienaCes8021xSuppSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 259),
    )


_CienaCes8021xSuppSecret_Type.__name__ = "OctetString"
_CienaCes8021xSuppSecret_Object = MibTableColumn
cienaCes8021xSuppSecret = _CienaCes8021xSuppSecret_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 18),
    _CienaCes8021xSuppSecret_Type()
)
cienaCes8021xSuppSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppSecret.setStatus("current")


class _CienaCes8021xSuppAdminState_Type(Integer32):
    """Custom type cienaCes8021xSuppAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppAdminState_Type.__name__ = "Integer32"
_CienaCes8021xSuppAdminState_Object = MibTableColumn
cienaCes8021xSuppAdminState = _CienaCes8021xSuppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 19),
    _CienaCes8021xSuppAdminState_Type()
)
cienaCes8021xSuppAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppAdminState.setStatus("current")


class _CienaCes8021xSuppEAPVersion_Type(Integer32):
    """Custom type cienaCes8021xSuppEAPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CienaCes8021xSuppEAPVersion_Type.__name__ = "Integer32"
_CienaCes8021xSuppEAPVersion_Object = MibTableColumn
cienaCes8021xSuppEAPVersion = _CienaCes8021xSuppEAPVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 20),
    _CienaCes8021xSuppEAPVersion_Type()
)
cienaCes8021xSuppEAPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppEAPVersion.setStatus("current")


class _CienaCes8021xSuppOCSPAdminState_Type(Integer32):
    """Custom type cienaCes8021xSuppOCSPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppOCSPAdminState_Type.__name__ = "Integer32"
_CienaCes8021xSuppOCSPAdminState_Object = MibTableColumn
cienaCes8021xSuppOCSPAdminState = _CienaCes8021xSuppOCSPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 21),
    _CienaCes8021xSuppOCSPAdminState_Type()
)
cienaCes8021xSuppOCSPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppOCSPAdminState.setStatus("current")


class _CienaCes8021xSuppCertificateName_Type(DisplayString):
    """Custom type cienaCes8021xSuppCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCes8021xSuppCertificateName_Type.__name__ = "DisplayString"
_CienaCes8021xSuppCertificateName_Object = MibTableColumn
cienaCes8021xSuppCertificateName = _CienaCes8021xSuppCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 22),
    _CienaCes8021xSuppCertificateName_Type()
)
cienaCes8021xSuppCertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppCertificateName.setStatus("current")


class _CienaCes8021xSuppMinimumTlsVersion_Type(Integer32):
    """Custom type cienaCes8021xSuppMinimumTlsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1dot0", 1),
          ("version1dot1", 2),
          ("version1dot2", 3))
    )


_CienaCes8021xSuppMinimumTlsVersion_Type.__name__ = "Integer32"
_CienaCes8021xSuppMinimumTlsVersion_Object = MibTableColumn
cienaCes8021xSuppMinimumTlsVersion = _CienaCes8021xSuppMinimumTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 23),
    _CienaCes8021xSuppMinimumTlsVersion_Type()
)
cienaCes8021xSuppMinimumTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppMinimumTlsVersion.setStatus("current")


class _CienaCes8021xSuppPeerCertReauthAdminState_Type(Integer32):
    """Custom type cienaCes8021xSuppPeerCertReauthAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CienaCes8021xSuppPeerCertReauthAdminState_Type.__name__ = "Integer32"
_CienaCes8021xSuppPeerCertReauthAdminState_Object = MibTableColumn
cienaCes8021xSuppPeerCertReauthAdminState = _CienaCes8021xSuppPeerCertReauthAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 2, 1, 24),
    _CienaCes8021xSuppPeerCertReauthAdminState_Type()
)
cienaCes8021xSuppPeerCertReauthAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppPeerCertReauthAdminState.setStatus("current")
_CienaCes8021xGlobalAttrs_ObjectIdentity = ObjectIdentity
cienaCes8021xGlobalAttrs = _CienaCes8021xGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 3)
)
_CienaCes8021xAuthStatsClear_Type = TruthValue
_CienaCes8021xAuthStatsClear_Object = MibScalar
cienaCes8021xAuthStatsClear = _CienaCes8021xAuthStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 3, 1),
    _CienaCes8021xAuthStatsClear_Type()
)
cienaCes8021xAuthStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xAuthStatsClear.setStatus("current")
_CienaCes8021xSuppStatsClear_Type = TruthValue
_CienaCes8021xSuppStatsClear_Object = MibScalar
cienaCes8021xSuppStatsClear = _CienaCes8021xSuppStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 2, 3, 2),
    _CienaCes8021xSuppStatsClear_Type()
)
cienaCes8021xSuppStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cienaCes8021xSuppStatsClear.setStatus("current")
_CienaCes8021xEvents_ObjectIdentity = ObjectIdentity
cienaCes8021xEvents = _CienaCes8021xEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 3)
)
_CienaCes8021xEventsV2_ObjectIdentity = ObjectIdentity
cienaCes8021xEventsV2 = _CienaCes8021xEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 42, 3, 0)
)
_CienaCes8021xMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCes8021xMIBNotificationPrefix = _CienaCes8021xMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101)
)
_CienaCes8021xMIBNotification_ObjectIdentity = ObjectIdentity
cienaCes8021xMIBNotification = _CienaCes8021xMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0)
)

# Managed Objects groups


# Notification objects

cienaCes8021xSuppAuthenticationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0, 1)
)
cienaCes8021xSuppAuthenticationEvent.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xPort"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xNotificationAuthenticationEvent"))
)
if mibBuilder.loadTexts:
    cienaCes8021xSuppAuthenticationEvent.setStatus(
        "current"
    )

cienaCes8021xAuthAuthenticationEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0, 2)
)
cienaCes8021xAuthAuthenticationEvent.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xPort"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xNotificationAuthenticationEvent"))
)
if mibBuilder.loadTexts:
    cienaCes8021xAuthAuthenticationEvent.setStatus(
        "current"
    )

cienaCes8021xGlobalStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0, 3)
)
cienaCes8021xGlobalStateChangeEvent.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("IEEE8021-PAE-MIB", "dot1xPaeSystemAuthControl"))
)
if mibBuilder.loadTexts:
    cienaCes8021xGlobalStateChangeEvent.setStatus(
        "current"
    )

cienaCes8021xAuthConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0, 4)
)
cienaCes8021xAuthConfigChangeEvent.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xPort"))
)
if mibBuilder.loadTexts:
    cienaCes8021xAuthConfigChangeEvent.setStatus(
        "current"
    )

cienaCes8021xSuppConfigChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 101, 0, 5)
)
cienaCes8021xSuppConfigChangeEvent.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-8021X-MIB", "cienaCes8021xPort"))
)
if mibBuilder.loadTexts:
    cienaCes8021xSuppConfigChangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-8021X-MIB",
    **{"cienaCes8021xMIB": cienaCes8021xMIB,
       "cienaCes8021xConf": cienaCes8021xConf,
       "cienaCes8021xGroups": cienaCes8021xGroups,
       "cienaCes8021xCompls": cienaCes8021xCompls,
       "cienaCes8021xObjs": cienaCes8021xObjs,
       "cienaCes8021xPortTable": cienaCes8021xPortTable,
       "cienaCes8021xPortEntry": cienaCes8021xPortEntry,
       "cienaCes8021xPort": cienaCes8021xPort,
       "cienaCes8021xRole": cienaCes8021xRole,
       "cienaCes8021xAuthPortStatsClear": cienaCes8021xAuthPortStatsClear,
       "cienaCes8021xNotificationAuthenticationEvent": cienaCes8021xNotificationAuthenticationEvent,
       "cienaCes8021xSuppTable": cienaCes8021xSuppTable,
       "cienaCes8021xSuppEntry": cienaCes8021xSuppEntry,
       "cienaCes8021xSuppPort": cienaCes8021xSuppPort,
       "cienaCes8021xSuppUserName": cienaCes8021xSuppUserName,
       "cienaCes8021xSuppPassword": cienaCes8021xSuppPassword,
       "cienaCes8021xSuppPortStatsClear": cienaCes8021xSuppPortStatsClear,
       "cienaCes8021xSuppEAPMethod": cienaCes8021xSuppEAPMethod,
       "cienaCes8021xSuppEAPAllowedMethods": cienaCes8021xSuppEAPAllowedMethods,
       "cienaCes8021xSuppOperationalState": cienaCes8021xSuppOperationalState,
       "cienaCes8021xSuppMutualAuthenticationAdminState": cienaCes8021xSuppMutualAuthenticationAdminState,
       "cienaCes8021xSuppCheckCertificateTimeAdminState": cienaCes8021xSuppCheckCertificateTimeAdminState,
       "cienaCes8021xSuppMutualAuthenticationOperState": cienaCes8021xSuppMutualAuthenticationOperState,
       "cienaCes8021xSuppCheckCertificateTimeOperState": cienaCes8021xSuppCheckCertificateTimeOperState,
       "cienaCes8021xSuppDeviceCertificateStatus": cienaCes8021xSuppDeviceCertificateStatus,
       "cienaCes8021xSuppSecret": cienaCes8021xSuppSecret,
       "cienaCes8021xSuppAdminState": cienaCes8021xSuppAdminState,
       "cienaCes8021xSuppEAPVersion": cienaCes8021xSuppEAPVersion,
       "cienaCes8021xSuppOCSPAdminState": cienaCes8021xSuppOCSPAdminState,
       "cienaCes8021xSuppCertificateName": cienaCes8021xSuppCertificateName,
       "cienaCes8021xSuppMinimumTlsVersion": cienaCes8021xSuppMinimumTlsVersion,
       "cienaCes8021xSuppPeerCertReauthAdminState": cienaCes8021xSuppPeerCertReauthAdminState,
       "cienaCes8021xGlobalAttrs": cienaCes8021xGlobalAttrs,
       "cienaCes8021xAuthStatsClear": cienaCes8021xAuthStatsClear,
       "cienaCes8021xSuppStatsClear": cienaCes8021xSuppStatsClear,
       "cienaCes8021xEvents": cienaCes8021xEvents,
       "cienaCes8021xEventsV2": cienaCes8021xEventsV2,
       "cienaCes8021xMIBNotificationPrefix": cienaCes8021xMIBNotificationPrefix,
       "cienaCes8021xMIBNotification": cienaCes8021xMIBNotification,
       "cienaCes8021xSuppAuthenticationEvent": cienaCes8021xSuppAuthenticationEvent,
       "cienaCes8021xAuthAuthenticationEvent": cienaCes8021xAuthAuthenticationEvent,
       "cienaCes8021xGlobalStateChangeEvent": cienaCes8021xGlobalStateChangeEvent,
       "cienaCes8021xAuthConfigChangeEvent": cienaCes8021xAuthConfigChangeEvent,
       "cienaCes8021xSuppConfigChangeEvent": cienaCes8021xSuppConfigChangeEvent}
)
